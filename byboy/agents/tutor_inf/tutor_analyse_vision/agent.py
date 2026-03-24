"""
导师主页**视觉**分析：``pic_find`` 从 HTML 拉取候选图至本包 ``cache/`` 子目录，
``pic_recog`` 逐张多模态结构化，再经 LLM 去重合并，最终输出形态与 ``tutor_analyse`` 一致。
"""

from __future__ import annotations

import asyncio
import hashlib
import json
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

from byboy.agent.invoke import AgentInvocation, ModelRef, slot_complete
from byboy.agents.tutor_inf.link_choose import LinkChooseError, parse_llm_json_object
from byboy.agents.tutor_inf.logging_utils import (
    AgentLogger,
    log_llm_wait_done,
    log_llm_wait_start,
    run_with_periodic_wait_log,
)
from byboy.agents.tutor_inf.tutor_analyse.agent import (
    TutorAnalysePayload,
    TutorAnalyseResult,
)
from byboy.agents.tutor_inf.tutor_analyse_vision.pic_find import (
    PicFindAgent,
    PicFindError,
    PicFindPayload,
)
from byboy.agents.tutor_inf.tutor_analyse_vision.pic_recog import (
    PicRecogAgent,
    PicRecogError,
    PicRecogPayload,
)
from byboy.llm.dispatcher import LLMDispatcher
from byboy.llm.route_spec import ChatMessage


class TutorAnalyseVisionError(RuntimeError):
    """视觉流水线失败（解析、子 agent 错误等）。"""


_CACHE_DIR = Path(__file__).resolve().parent / "cache"


def _markdown_cache_filename(url: str) -> str:
    h = hashlib.sha256(url.strip().encode("utf-8")).hexdigest()
    return f"{h}.md"


def _output_path(output_dir: str | Path, output_filename: str) -> Path:
    name = output_filename.strip()
    if not name:
        raise ValueError("output_filename 不能为空")
    return (Path(output_dir) / name).resolve()


MERGE_SYSTEM_PROMPT = """你是 JSON 合并助手。用户会提供同一导师个人主页上**多张图片**的视觉抽取结果：每项为一张图对应的 JSON 对象（已尽量穷尽图中信息）。

【硬性要求】
- 将多份片段**合并为单个 JSON 对象**（可任意嵌套、任意键名），风格与上游视觉抽取保持一致，例如用带 tags 的 blocks / sections 等组织。
- **仅做去重与合并**：完全相同的条目合并为一项；高度重叠的内容合并为一条时，须保留差异要点（如不同图片来源下的表述）。
- **禁止**因主观判断「次要」「无关」「重复」而删除信息；若无法判断是否同一事实，**宁可保留**多条并注明来源图片文件名。
- **禁止**输出 Markdown 代码围栏；**禁止**在 JSON 外附加解释文字。

请只输出 JSON。"""


class TutorAnalyseVisionAgent:
    """协调 ``pic_find``、``pic_recog`` 与最终合并 LLM；对外载荷与 ``TutorAnalyseAgent`` 相同。"""

    def run(
        self,
        inv: AgentInvocation[TutorAnalysePayload],
        dispatcher: LLMDispatcher,
        *,
        max_tokens: int = 16384,
        merge_max_tokens: int | None = None,
    ) -> TutorAnalyseResult:
        log = AgentLogger("TutorAnalyseVisionAgent")
        dispatcher.resolve(inv.model.token)
        p = inv.llm_part
        log.start("开始视觉导师页分析", detail=f"name={p.tutor_name_cn.strip()} url={p.url.strip()}")
        merge_cap = merge_max_tokens if merge_max_tokens is not None else max_tokens

        cache_dir = _CACHE_DIR
        cache_dir.mkdir(parents=True, exist_ok=True)
        session = cache_dir / hashlib.sha256(p.url.strip().encode("utf-8")).hexdigest()
        session.mkdir(parents=True, exist_ok=True)
        images_dir = session / "images"
        images_dir.mkdir(parents=True, exist_ok=True)

        md_name = _markdown_cache_filename(p.url)
        md_path = (cache_dir / md_name).resolve()
        stub_lines = [
            f"> 抓取来源：{p.url.strip()}",
            "",
            "> tutor_analyse_vision：由 HTML 抽取图片并走视觉识别；本 Markdown 仅为与 tutor_analyse 对齐的溯源占位。",
        ]
        if p.markdown_path is not None:
            stub_lines.append(
                f"> 注意：已提供 markdown_path={p.markdown_path!s}；本视觉流水线仍从 request_url 拉取 HTML 用于找图。"
            )
        md_path.write_text("\n".join(stub_lines) + "\n", encoding="utf-8", newline="\n")

        try:
            log.step("调用 PicFind 提取候选图片")
            pf = PicFindAgent().run(
                AgentInvocation(
                    model=inv.model,
                    llm_part=PicFindPayload(url=p.url.strip(), output_dir=images_dir),
                ),
                dispatcher,
            )
        except PicFindError as e:
            raise TutorAnalyseVisionError(str(e)) from e

        declared_source: str | None = None
        try:
            man = json.loads(pf.manifest_path.read_text(encoding="utf-8"))
            declared_source = str(man.get("resolved_page_url") or "").strip() or None
        except (OSError, json.JSONDecodeError):
            declared_source = None

        pr_agent = PicRecogAgent()
        fragments: list[dict[str, Any]] = []
        sidecar_paths: list[str] = []
        log.step("开始逐图识别", detail=f"images={len(pf.image_paths)}")
        for img_path in sorted(pf.image_paths, key=lambda x: x.name):
            try:
                r = pr_agent.run(
                    AgentInvocation(
                        model=inv.model,
                        llm_part=PicRecogPayload(
                            image_path=img_path,
                            tutor_name_cn=p.tutor_name_cn,
                        ),
                    ),
                    dispatcher,
                    max_tokens=max_tokens,
                )
            except PicRecogError as e:
                raise TutorAnalyseVisionError(str(e)) from e
            sidecar_paths.append(str(r.json_path))
            try:
                one = json.loads(r.json_path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError) as e:
                raise TutorAnalyseVisionError(f"读取侧车 JSON 失败: {r.json_path}") from e
            ex = one.get("extracted")
            if not isinstance(ex, dict):
                ex = {}
            fragments.append({"source_image": one.get("source_image"), "extracted": ex})
            log.info("完成单图识别", detail=img_path.name)

        if fragments:
            log.step("合并多图结构化结果", detail=f"fragments={len(fragments)}")
            merge_messages: list[ChatMessage] = [
                {"role": "system", "content": MERGE_SYSTEM_PROMPT},
                {
                    "role": "user",
                    "content": json.dumps({"fragments": fragments}, ensure_ascii=False),
                },
            ]
            t0 = log_llm_wait_start(
                log,
                model=inv.model.token,
                payload=merge_messages,
                max_tokens=merge_cap,
                stage="vision_merge",
            )
            raw = run_with_periodic_wait_log(
                log=log,
                stage="vision_merge",
                wait_message="等待模型响应中",
                every_sec=5.0,
                fn=lambda: slot_complete(
                    dispatcher,
                    inv.model.token,
                    merge_messages,
                    max_tokens=merge_cap,
                ),
            )
            log_llm_wait_done(log, stage="vision_merge", started_at=t0)
            try:
                merged = parse_llm_json_object(raw)
            except LinkChooseError as e:
                raise TutorAnalyseVisionError(str(e)) from e
            if not isinstance(merged, dict):
                raise TutorAnalyseVisionError("合并阶段模型输出 JSON 根节点必须是对象")
            extracted: dict[str, Any] = merged
        else:
            extracted = {}

        meta = {
            "tutor_name_cn": p.tutor_name_cn.strip(),
            "request_url": p.url.strip(),
            "declared_source_url": declared_source,
            "page_host": urlsplit(declared_source).netloc if declared_source else urlsplit(p.url.strip()).netloc,
            "markdown_cache_path": str(md_path),
            "markdown_source": "tutor_analyse_vision_stub",
            "vision_session_dir": str(session.resolve()),
            "vision_image_cache_dir": str(images_dir.resolve()),
            "vision_manifest_path": str(pf.manifest_path.resolve()),
            "vision_per_image_json": sidecar_paths,
            "pipeline": "tutor_analyse_vision",
        }
        out_obj = {"meta": meta, "extracted": extracted}
        out = _output_path(p.output_dir, p.output_filename)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(
            json.dumps(out_obj, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        log.done("视觉分析完成", detail=str(out))
        return TutorAnalyseResult(json_path=out, markdown_cache_path=md_path)

    async def arun(
        self,
        inv: AgentInvocation[TutorAnalysePayload],
        dispatcher: LLMDispatcher,
        *,
        max_tokens: int = 16384,
        merge_max_tokens: int | None = None,
    ) -> TutorAnalyseResult:
        return await asyncio.to_thread(
            self.run, inv, dispatcher, max_tokens=max_tokens, merge_max_tokens=merge_max_tokens
        )


__all__ = [
    "AgentInvocation",
    "ModelRef",
    "TutorAnalysePayload",
    "TutorAnalyseResult",
    "TutorAnalyseVisionAgent",
    "TutorAnalyseVisionError",
]
