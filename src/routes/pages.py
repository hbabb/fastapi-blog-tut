from fastapi import APIRouter, Request

from src.core.templating import templates
from src.sample_posts import posts

router = APIRouter(include_in_schema=False)


@router.get("/", name="home")
def home(request: Request):
    return templates.TemplateResponse(
        request,
        "home.html",
        {"posts": posts, "title": "Home"},
    )


@router.get("/posts", name="posts")
def all_posts(request: Request):
    return templates.TemplateResponse(
        request,
        "home.html",
        {"posts": posts, "title": "Posts"},
    )
