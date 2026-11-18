from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path.cwd() / ".env")


@dataclass(frozen=True)
class AppConfig:
    base_url: str


env = AppConfig(
    base_url=os.getenv("BASE_URL", "https://serverest.dev"),
)
