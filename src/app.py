import structlog
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi_swagger_ui_theme import setup_swagger_ui_theme

from src.core.config import settings
from src.core.logging import configure_logging
from src.core.project import PROJECT_NAME, PROJECT_VERSION
from src.posts.data import posts

configure_logging(settings.log_level, settings.log_json)

log = structlog.get_logger(__name__)

app = FastAPI(
    title="FastAPI Blog Tutorial",
    docs_url=None,
)
setup_swagger_ui_theme(app, docs_path="/docs")


@app.get("/", tags=["home"], response_class=HTMLResponse, include_in_schema=False)
@app.get("/posts", tags=["posts"], response_class=HTMLResponse, include_in_schema=False)
def home():
    return f"<h1>{posts[0]['title']}</h1>"


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
