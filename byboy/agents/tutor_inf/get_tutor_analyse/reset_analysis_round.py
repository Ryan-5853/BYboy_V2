"""
按 get_tutor_pages 写入的 ``records[].round`` 清除分析断点：
从 ``list4_analysed_profiles`` 移除对应 URL、删掉 ``records`` 中的 analysed_* 字段，
并删除磁盘上的 analysed JSON（若存在）。
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Any


def _read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8", errors="replace"))


def _write_json(path: Path, obj: Any) -> None:
    path.write_text(
        json.dumps(obj, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def _resolve_analysed_json(workspace: Path, analysed_file: str) -> Path | None:
    """匹配 state 里存的相对路径或仅 basename。"""
    s = (analysed_file or "").strip()
    if not s:
        return None
    p = Path(s)
    candidates = [
        workspace / "cache" / "analysed" / p.name,
        workspace.parent / p,
        Path.cwd() / s,
        p if p.is_absolute() else None,
    ]
    for c in candidates:
        if c is None:
            continue
        try:
            r = c.resolve()
        except OSError:
            continue
        if r.is_file():
            return r
    return None


def reset_analysis_round(
    workspace_dir: str | Path,
    *,
    target_round: int,
    dry_run: bool = False,
) -> dict[str, Any]:
    """
    :param workspace_dir: get_tutor_pages 工作目录（含 ``cache/state.json``）
    :param target_round: 与 ``records[].round`` 相等的轮次（如第二轮为 ``2``）
    :return: 统计信息 dict
    """
    if target_round < 1:
        raise ValueError("target_round 必须 >= 1")
    workspace = Path(workspace_dir).resolve()
    state_path = (workspace / "cache" / "state.json").resolve()
    if not state_path.is_file():
        raise FileNotFoundError(f"state.json 不存在: {state_path}")

    state = _read_json(state_path)
    if not isinstance(state, dict):
        raise ValueError("state.json 根节点必须是对象")
    records = state.get("records")
    if not isinstance(records, list):
        raise ValueError("state.records 必须是数组")

    round_urls: set[str] = set()
    files_to_delete: list[Path] = []
    cleared_records = 0

    for rec in records:
        if not isinstance(rec, dict):
            continue
        if int(rec.get("round", -1)) != target_round:
            continue
        url = str(rec.get("url") or "").strip()
        if url:
            round_urls.add(url)
        af = rec.get("analysed_file")
        if isinstance(af, str) and af.strip():
            hit = _resolve_analysed_json(workspace, af)
            if hit is not None:
                files_to_delete.append(hit)
        if "analysed_file" in rec or "analysed_name" in rec:
            cleared_records += 1
        rec.pop("analysed_file", None)
        rec.pop("analysed_name", None)

    list4 = state.get("list4_analysed_profiles")
    if not isinstance(list4, list):
        list4 = []
    before_l4 = len(list4)
    new_l4 = [u for u in list4 if str(u).strip() not in round_urls]
    state["list4_analysed_profiles"] = sorted(new_l4)

    manifest_path = (workspace / "cache" / "analysed" / "manifest.json").resolve()
    manifest_updated = False
    if manifest_path.is_file():
        man = _read_json(manifest_path)
        if isinstance(man, dict):
            ok = man.get("success_items")
            if isinstance(ok, list):
                man["success_items"] = [
                    x
                    for x in ok
                    if isinstance(x, dict)
                    and str(x.get("url") or "").strip() not in round_urls
                ]
            man["success_count"] = len(man.get("success_items") or [])
            sk = man.get("skipped_items")
            if isinstance(sk, list):
                man["skipped_items"] = [
                    x
                    for x in sk
                    if isinstance(x, dict)
                    and str(x.get("url") or "").strip() not in round_urls
                ]
            man["skipped_count"] = len(man.get("skipped_items") or [])
            if not dry_run:
                _write_json(manifest_path, man)
            manifest_updated = True

    deleted_files: list[str] = []
    if not dry_run:
        _write_json(state_path, state)
        seen: set[Path] = set()
        for fp in files_to_delete:
            rp = fp.resolve()
            if rp in seen:
                continue
            seen.add(rp)
            try:
                rp.unlink()
                deleted_files.append(os.path.relpath(str(rp), str(Path.cwd())))
            except OSError:
                pass

    return {
        "workspace": str(workspace),
        "target_round": target_round,
        "round_url_count": len(round_urls),
        "list4_removed": before_l4 - len(new_l4),
        "records_cleared_fields": cleared_records,
        "json_files_deleted": len(deleted_files),
        "deleted_paths": deleted_files,
        "dry_run": dry_run,
        "manifest_touched": manifest_updated,
    }


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="按抓取轮次清除导师分析断点（list4 + records.analysed_* + analysed/*.json）"
    )
    p.add_argument(
        "workspace_dir",
        nargs="?",
        type=Path,
        help="工作目录；可改用 --workdir",
    )
    p.add_argument("--workdir", type=Path, default=None, help="等价 workspace_dir")
    p.add_argument(
        "--round",
        type=int,
        required=True,
        dest="target_round",
        help="与 state.records[].round 一致的轮次，例如第二轮填 2",
    )
    p.add_argument(
        "--dry-run",
        action="store_true",
        help="只打印将执行的操作，不写盘、不删文件",
    )
    args = p.parse_args(argv)
    wd = args.workdir or args.workspace_dir
    if wd is None:
        raise SystemExit("必须提供 workspace_dir 或 --workdir")
    info = reset_analysis_round(wd, target_round=args.target_round, dry_run=args.dry_run)
    print(json.dumps(info, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
