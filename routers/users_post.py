from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["user"]
)

@router.post('/new')
def create_new_user():
    pass
