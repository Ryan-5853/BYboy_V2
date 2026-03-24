"""从仓库/当前工作目录附近的 ``.env`` 注入环境变量（幂等）。"""

from __future__ import annotations

_loaded = False


def ensure_dotenv_loaded() -> None:
    """在项目任意代码读取 ``os.environ`` 前调用，确保已加载 ``.env``。"""
    global _loaded
    if _loaded:
        return
    try:
        from dotenv import find_dotenv, load_dotenv

        path = find_dotenv(usecwd=True)
        if path:
            load_dotenv(path)
    except ImportError:
        pass
    _loaded = True
