"""
将 analysed/*.json（导师信息自由结构 JSON）经 LLM 解释后，汇总为固定列 CSV。
"""

from __future__ import annotations

import asyncio
import csv
import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from byboy.agent.invoke import AgentInvocation, ModelRef, agent_complete, slot_complete
from byboy.agents.tutor_inf.link_choose import LinkChooseError, parse_llm_json_object
from byboy.agents.tutor_inf.logging_utils import (
    AgentLogger,
    log_llm_wait_done,
    log_llm_wait_start,
    run_with_periodic_wait_log,
)
from byboy.llm.dispatcher import LLMDispatcher
from byboy.llm.route_spec import ChatMessage


class OutputToCsvError(RuntimeError):
    """CSV 输出阶段失败。"""


CSV_HEADERS: tuple[str, ...] = (
    "学校",
    "院系",
    "导师姓名",
    "性别",
    "年龄",
    "所属实验室",
    "研究方向",
    "招生指标",
    "招生要求",
    "联系方式",
    "邮箱",
    "地址",
    "教育背景",
    "职称",
    "荣誉",
    "在研项目",
    "学术成果",
)

EXTRACT_SCHEMA_VERSION = 2


SYSTEM_PROMPT = """你是导师信息抽取助手。用户会提供一个导师分析 JSON（字段不固定）。

请你只输出一个 JSON 对象，且必须严格包含以下键（一个都不能少）：
- 学校
- 院系
- 导师姓名
- 性别
- 年龄
- 所属实验室
- 研究方向
- 招生指标
- 招生要求
- 联系方式
- 邮箱
- 地址
- 教育背景
- 职称
- 荣誉
- 在研项目
- 学术成果

抽取规则：
1) 仅依据输入 JSON 中已有信息推断，禁止编造。
2) 如果没有对应信息，值必须是空字符串 ""。
3) 输出值全部为字符串，不要输出数组/对象/null。
4) 若存在多个候选，优先更具体、置信更高、与导师本人直接相关的信息。
5) “联系方式”可填电话/微信/主页链接等非邮箱联系信息；“邮箱”单独填写。
6) “在研项目”请只保留仍在进行中的项目；若有多个，请按重要性从高到低排序后合并为单个字符串（建议以分号分隔）。
7) “学术成果”需要你做简要总结：优先概括论文/专著/专利/奖项等高价值成果，形成 1-3 句中文摘要；不要逐条机械罗列。
8) “教育背景”优先提取学校、学位、时间等关键要素并合并为单个字符串。
9) “荣誉”优先保留高层级、代表性强且与科研教学相关的荣誉；多个荣誉按重要性从高到低排序后合并为单个字符串。
10) 禁止输出代码围栏，禁止在 JSON 外输出任何解释文字。
"""


SYSTEM_JSON_REPAIR = """你是 JSON 语法修复助手。用户会给你一段本应是单个 JSON 对象的文本，
其中可能有未转义引号、尾逗号、代码围栏或夹杂说明文字。

请只输出一个可被标准 json.loads 解析的 JSON 对象，尽量保留原字段与语义。
禁止输出 JSON 以外的任何内容。"""


@dataclass(frozen=True, slots=True)
class OutputToCsvPayload:
    analysed_dir: str | Path
    csv_path: str | Path
    resume_state_path: str | Path | None = None
    run_log_path: str | Path | None = None


@dataclass(frozen=True, slots=True)
class OutputToCsvResult:
    analysed_dir: Path
    csv_path: Path
    scanned_count: int
    parsed_count: int
    appended_count: int
    updated_count: int
    skipped_count: int


def _normalize_cell(v: Any) -> str:
    if isinstance(v, str):
        return v.strip()
    if v is None:
        return ""
    return str(v).strip()


def _normalize_row(raw: dict[str, Any]) -> dict[str, str]:
    out: dict[str, str] = {}
    for k in CSV_HEADERS:
        out[k] = _normalize_cell(raw.get(k, ""))
    return out


def _read_existing_rows(csv_path: Path) -> list[dict[str, str]]:
    if not csv_path.is_file():
        return []
    with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        rows: list[dict[str, str]] = []
        for r in reader:
            if not isinstance(r, dict):
                continue
            rows.append(_normalize_row(r))
        return rows


def _write_rows(csv_path: Path, rows: list[dict[str, str]]) -> None:
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with csv_path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(CSV_HEADERS))
        writer.writeheader()
        for r in rows:
            writer.writerow({k: _normalize_cell(r.get(k, "")) for k in CSV_HEADERS})


def _sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8", errors="replace")).hexdigest()


def _read_json(path: Path, default_obj: Any) -> Any:
    if not path.is_file():
        return default_obj
    try:
        return json.loads(path.read_text(encoding="utf-8", errors="replace"))
    except json.JSONDecodeError:
        return default_obj


def _write_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(obj, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def _append_jsonl(path: Path, obj: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(obj, ensure_ascii=False) + "\n")


def _identity_key(row: dict[str, str]) -> tuple[str, str, str]:
    return (row["学校"], row["院系"], row["导师姓名"])


def _fallback_key(row: dict[str, str]) -> tuple[str, str, str]:
    return ("", "", row["导师姓名"])


def _merge_non_empty(dst: dict[str, str], src: dict[str, str]) -> tuple[dict[str, str], bool]:
    changed = False
    out = dict(dst)
    for k in CSV_HEADERS:
        nv = _normalize_cell(src.get(k, ""))
        if not nv:
            continue
        if _normalize_cell(out.get(k, "")) == nv:
            continue
        out[k] = nv
        changed = True
    return out, changed


def _build_user_content(obj: dict[str, Any], src_name: str) -> str:
    return (
        f"来源文件：{src_name}\n"
        "请按系统要求抽取固定字段。\n"
        "注意：涉及“项目”“荣誉”等多条目内容时，请按重要性降序重排。\n"
        "----- 输入 JSON 开始 -----\n"
        f"{json.dumps(obj, ensure_ascii=False, indent=2)}\n"
        "----- 输入 JSON 结束 -----"
    )


def _parse_with_repair(
    raw: str,
    dispatcher: LLMDispatcher,
    slot_token: str,
    *,
    repair_max_tokens: int,
    log: AgentLogger | None = None,
    stage: str = "json_repair",
) -> dict[str, Any]:
    try:
        obj = parse_llm_json_object(raw)
    except LinkChooseError:
        repair_messages: list[ChatMessage] = [
            {"role": "system", "content": SYSTEM_JSON_REPAIR},
            {
                "role": "user",
                "content": "以下内容无法被 json.loads 解析，请修复为合法 JSON 对象：\n\n" + raw.strip()[:120_000],
            },
        ]
        t0 = None
        if log is not None:
            t0 = log_llm_wait_start(
                log,
                model=slot_token,
                payload=repair_messages,
                max_tokens=repair_max_tokens,
                stage=stage,
            )
        fixed = run_with_periodic_wait_log(
            log=log if log is not None else AgentLogger("OutputToCsvAgent"),
            stage=stage,
            wait_message="等待模型响应中",
            every_sec=5.0,
            fn=lambda: slot_complete(
                dispatcher,
                slot_token,
                repair_messages,
                max_tokens=repair_max_tokens,
            ),
        )
        if log is not None and t0 is not None:
            log_llm_wait_done(log, stage=stage, started_at=t0)
        obj = parse_llm_json_object(fixed)
    if not isinstance(obj, dict):
        raise OutputToCsvError("模型输出 JSON 根节点必须是对象")
    return obj


class OutputToCsvAgent:
    def run(
        self,
        inv: AgentInvocation[OutputToCsvPayload],
        dispatcher: LLMDispatcher,
        *,
        max_tokens: int = 2048,
        repair_max_tokens: int = 4096,
    ) -> OutputToCsvResult:
        log = AgentLogger("OutputToCsvAgent")
        if max_tokens <= 0 or repair_max_tokens <= 0:
            raise ValueError("max_tokens 与 repair_max_tokens 必须为正整数")
        dispatcher.resolve(inv.model.token)
        p = inv.llm_part
        analysed_dir = Path(p.analysed_dir).resolve()
        csv_path = Path(p.csv_path).resolve()
        resume_state_path = (
            Path(p.resume_state_path).resolve()
            if p.resume_state_path is not None
            else (analysed_dir.parent / "cache" / "output_to_csv.resume.json").resolve()
        )
        run_log_path = (
            Path(p.run_log_path).resolve()
            if p.run_log_path is not None
            else (analysed_dir.parent / "cache" / "run_output_to_csv.jsonl").resolve()
        )
        log.start("开始汇总 CSV", detail=f"analysed={analysed_dir}")
        if not analysed_dir.is_dir():
            raise FileNotFoundError(f"analysed_dir 不存在: {analysed_dir}")

        source_files = sorted(
            [x for x in analysed_dir.glob("*.json") if x.name.lower() != "manifest.json"]
        )
        log.step("扫描 analysed JSON", detail=f"count={len(source_files)}")
        existing_rows = _read_existing_rows(csv_path)
        rows = [dict(r) for r in existing_rows]
        by_key: dict[tuple[str, str, str], int] = {}
        by_name_key: dict[tuple[str, str, str], int] = {}
        for i, r in enumerate(rows):
            k = _identity_key(r)
            if k not in by_key:
                by_key[k] = i
            nk = _fallback_key(r)
            if nk not in by_name_key:
                by_name_key[nk] = i

        resume_obj = _read_json(
            resume_state_path,
            default_obj={"schema_version": EXTRACT_SCHEMA_VERSION, "files": {}},
        )
        if not isinstance(resume_obj, dict):
            resume_obj = {"schema_version": EXTRACT_SCHEMA_VERSION, "files": {}}
        if resume_obj.get("schema_version") != EXTRACT_SCHEMA_VERSION:
            resume_obj = {"schema_version": EXTRACT_SCHEMA_VERSION, "files": {}}
        resume_files = resume_obj.get("files")
        if not isinstance(resume_files, dict):
            resume_files = {}
            resume_obj["files"] = resume_files

        parsed_count = 0
        appended_count = 0
        updated_count = 0
        skipped_count = 0

        for i, fp in enumerate(source_files, start=1):
            log.step("处理 analysed 文件", detail=f"{i}/{len(source_files)} {fp.name}")
            raw_text = fp.read_text(encoding="utf-8", errors="replace")
            source_hash = _sha256_text(raw_text)
            row: dict[str, str] | None = None
            cached = resume_files.get(fp.name)
            if isinstance(cached, dict) and cached.get("source_hash") == source_hash:
                maybe_row = cached.get("row")
                if isinstance(maybe_row, dict):
                    row = _normalize_row(maybe_row)
                    parsed_count += 1
                    log.info("命中断点缓存", detail=fp.name)

            obj: dict[str, Any] | None = None
            if row is None:
                try:
                    loaded = json.loads(raw_text)
                except json.JSONDecodeError:
                    skipped_count += 1
                    _append_jsonl(
                        run_log_path,
                        {"file": fp.name, "status": "skipped", "reason": "invalid_json"},
                    )
                    continue
                if not isinstance(loaded, dict):
                    skipped_count += 1
                    _append_jsonl(
                        run_log_path,
                        {"file": fp.name, "status": "skipped", "reason": "root_not_object"},
                    )
                    continue
                obj = loaded

                messages: list[ChatMessage] = [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": _build_user_content(obj, fp.name)},
                ]
                t1 = log_llm_wait_start(
                    log,
                    model=inv.model.token,
                    payload=messages,
                    max_tokens=max_tokens,
                    stage=f"extract_{fp.name}",
                )
                raw = run_with_periodic_wait_log(
                    log=log,
                    stage=f"extract_{fp.name}",
                    wait_message="等待模型响应中",
                    every_sec=5.0,
                    fn=lambda: agent_complete(
                        dispatcher,
                        AgentInvocation(model=inv.model, llm_part=messages),
                        max_tokens=max_tokens,
                    ),
                )
                log_llm_wait_done(log, stage=f"extract_{fp.name}", started_at=t1)
                out_obj = _parse_with_repair(
                    raw,
                    dispatcher,
                    inv.model.token,
                    repair_max_tokens=repair_max_tokens,
                    log=log,
                    stage=f"json_repair_{fp.name}",
                )
                row = _normalize_row(out_obj)
                parsed_count += 1

            if not row["导师姓名"]:
                meta = (obj or {}).get("meta")
                if isinstance(meta, dict):
                    row["导师姓名"] = _normalize_cell(meta.get("tutor_name_cn", ""))

            resume_files[fp.name] = {"source_hash": source_hash, "row": row}
            _write_json(resume_state_path, resume_obj)

            if not row["导师姓名"]:
                skipped_count += 1
                log.warn("跳过记录", detail=f"{fp.name} 缺少导师姓名")
                _append_jsonl(
                    run_log_path,
                    {"file": fp.name, "status": "skipped", "reason": "missing_tutor_name"},
                )
                continue

            key = _identity_key(row)
            if any(key):
                idx = by_key.get(key)
            else:
                idx = None
            if idx is None:
                idx = by_name_key.get(_fallback_key(row))

            if idx is None:
                rows.append(row)
                new_idx = len(rows) - 1
                by_key[_identity_key(row)] = new_idx
                by_name_key[_fallback_key(row)] = new_idx
                appended_count += 1
                log.info("追加新行", detail=row["导师姓名"])
                _append_jsonl(
                    run_log_path,
                    {"file": fp.name, "tutor": row["导师姓名"], "status": "appended"},
                )
                continue

            merged, changed = _merge_non_empty(rows[idx], row)
            if changed:
                rows[idx] = merged
                by_key[_identity_key(merged)] = idx
                by_name_key[_fallback_key(merged)] = idx
                updated_count += 1
                log.info("更新已有行", detail=row["导师姓名"])
                _append_jsonl(
                    run_log_path,
                    {"file": fp.name, "tutor": row["导师姓名"], "status": "updated"},
                )
            else:
                _append_jsonl(
                    run_log_path,
                    {"file": fp.name, "tutor": row["导师姓名"], "status": "unchanged"},
                )

        _write_rows(csv_path, rows)
        _write_json(resume_state_path, resume_obj)
        log.done(
            "CSV 输出完成",
            detail=f"parsed={parsed_count} appended={appended_count} updated={updated_count} skipped={skipped_count}",
        )
        return OutputToCsvResult(
            analysed_dir=analysed_dir,
            csv_path=csv_path,
            scanned_count=len(source_files),
            parsed_count=parsed_count,
            appended_count=appended_count,
            updated_count=updated_count,
            skipped_count=skipped_count,
        )

    async def arun(
        self,
        inv: AgentInvocation[OutputToCsvPayload],
        dispatcher: LLMDispatcher,
        *,
        max_tokens: int = 2048,
        repair_max_tokens: int = 4096,
    ) -> OutputToCsvResult:
        return await asyncio.to_thread(
            self.run,
            inv,
            dispatcher,
            max_tokens=max_tokens,
            repair_max_tokens=repair_max_tokens,
        )


__all__ = [
    "AgentInvocation",
    "ModelRef",
    "OutputToCsvAgent",
    "OutputToCsvError",
    "OutputToCsvPayload",
    "OutputToCsvResult",
]
