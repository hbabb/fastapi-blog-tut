from pathlib import Path

import structlog
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi_swagger_ui_theme import setup_swagger_ui_theme

from src.core.config import settings
from src.core.logging import configure_logging
from src.core.project import PROJECT_NAME, PROJECT_VERSION
from src.posts.data import posts

BASE_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"

configure_logging(settings.log_level, settings.log_json)

log = structlog.get_logger(__name__)

app = FastAPI(
    title="FastAPI Blog Tutorial",
    docs_url=None,
)
setup_swagger_ui_theme(app, docs_path="/docs")

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

templates = Jinja2Templates(directory=TEMPLATES_DIR)


@app.get("/", tags=["home"], include_in_schema=False, name="home")
@app.get("/posts", tags=["posts"], include_in_schema=False, name="posts")
def home(request: Request):
    return templates.TemplateResponse(
        request,
        "home.html",
        {"posts": posts, "title": "Home"},
    )


@app.get("/api/posts", tags=["posts api"])
def get_posts():
    return posts


@app.get("/health", tags=["health"])
def health_check() -> dict[str, str]:
    return {
        "status": "ok",
        "name": PROJECT_NAME,
        "version": PROJECT_VERSION,
    }
