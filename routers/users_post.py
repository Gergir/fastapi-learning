from typing import Optional, List, Dict

from fastapi import APIRouter, Query, Body, Path
from pydantic import BaseModel

router = APIRouter(
    prefix="/users",
    tags=["user"]
)


class Image(BaseModel):
    url: str
    alias: str


class UserModel(BaseModel):
    username: str
    password: str
    description: Optional[str]
    public_user: Optional[bool]
    tags: List[str] = []
    metadata: Dict[str, str] = {"key": "value"}
    image: Optional[Image] = None


@router.post('/new/{user_id}')
def create_new_user(user: UserModel, user_id: int, version: int = 1):
    return {
        "id": user_id,
        "user": user,
        "version": version
    }


@router.post("/new/{user_id}/post/{post_id}")
def create_new_post(
        user: UserModel,
        user_id: int,
        post_id: int = Path(
            ge=1,
            le=100
        ),
        post_title: str = Query(
            None,
            title="title of the post",
            description="This is the title of the current post",
            alias="postTitle",  # defines how the parameter is provided in the request '?postId=...', it is converted
            # back at the response
            deprecated=True
        ),

        content: str = Body(
            ...,
            min_length=10,
            max_length=50,
            regex='^[a-z\s]*$'
        ),
        post_version: Optional[List[str]] = Query(["1.0", "1.1", "1.2"])
):
    return {
        "user_id": user_id,
        "post_id": post_id,
        "user": user,
        "post_title": post_title,
        "content": content,
        "post_version": post_version
    }
