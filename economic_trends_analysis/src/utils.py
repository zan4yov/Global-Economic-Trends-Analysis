from __future__ import annotations
import os
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parents[1]

def ensure_dirs():
    (BASE_DIR / "data").mkdir(parents=True, exist_ok=True)

def get_env(var: str, default: Optional[str] = None) -> Optional[str]:
    # Load .env if present
    load_dotenv(BASE_DIR / ".env", override=False)
    return os.getenv(var, default)
