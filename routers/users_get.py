from fastapi import APIRouter, status, Response, Depends
from enum import Enum
from typing import Optional

from routers.users_post import required_function

router = APIRouter(
    prefix="/users",
    tags=["user"]
)


class UserType(str, Enum):
    admin = "admin"
    standard_user = "standard"
    tech_user = "tech"


@router.get("/")
def hello():
    return {"message": "hello world!"}


@router.get("/all")
def get_all_users(
                user_count: int = 10,
                user_type: UserType = UserType.standard_user,
                required_parameter: dict = Depends(required_function)
):
    """
    Simulates fetching data of all users

    - **user_count** optional query parameter
    - **user_type** optional query parameter
    """
    return {"message": f"fetching {user_count} {user_type.value} users. Required_param: {required_parameter}"}


@router.get(
    "/{user_id}/description/{description_id}",
    tags=["comment"],
    summary="Get the description",
    description="Get the specified description of specified user",
    response_description="description json2"

)
def get_user_description(user_id: int, description_id: int, valid=True, username: Optional[str] = None):
    return {"user_id": user_id}, {"description_id": description_id}, {"valid": valid}, {"username": username}


@router.get("/type/{user_type}")
def get_user_type(user_type: UserType):
    return {"message": f"user type: {user_type}"}


@router.get("/{user_id}")
def get_user(user_id: int, response: Response):
    if user_id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": "404 not found"}
    response.status_code = status.HTTP_200_OK
    return {"message": f"user with {user_id} has been returned"}

# The order is important - first more specific one
# fastapi will evaluate paths one by one
