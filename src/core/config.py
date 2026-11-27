import os
from pathlib import Path

from dotenv import load_dotenv
from pydantic import BaseModel, ConfigDict, Field

# src/core/config.py -> repository root, where .env lives.
REPO_ROOT = Path(__file__).resolve().parents[2]


class Settings(BaseModel):
    model_config = ConfigDict(frozen=True)

    database_url: str = Field(default="sqlite+aisqlite:///./blog.db", alias="DATABASE_URL")
    api_host: str = Field(default="127.0.0.1", alias="API_HOST")
    api_port: int = Field(default=8000, alias="API_PORT")
    log_level: str = Field(default="INFO", alias="LOG_LEVEL")
    log_json: bool = Field(default=False, alias="LOG_JSON")


_ = load_dotenv(REPO_ROOT / ".env")
settings = Settings.model_validate(os.environ)
