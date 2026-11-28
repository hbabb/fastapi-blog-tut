import structlog
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi_swagger_ui_theme import setup_swagger_ui_theme

from src.core.config import STATIC_DIR, settings
from src.core.logging import configure_logging
from src.core.project import PROJECT_NAME, PROJECT_VERSION
from src.routes import api, pages

configure_logging(settings.log_level, settings.log_json)

log = structlog.get_logger(__name__)

app = FastAPI(
    title=PROJECT_NAME,
    docs_url=None,
)
setup_swagger_ui_theme(app, docs_path="/docs")

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

app.include_router(pages.router)

app.include_router(api.router)


@app.get("/health", tags=["health"])
def health_check() -> dict[str, str]:
    return {
        "status": "ok",
        "name": PROJECT_NAME,
        "version": PROJECT_VERSION,
    }
