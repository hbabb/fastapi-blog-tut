from fastapi import APIRouter

from src.sample_posts import posts

router = APIRouter()


@router.get("/api/posts", tags=["posts api"])
def get_posts():
    return posts
