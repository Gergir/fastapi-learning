from typing import List
from fastapi import APIRouter, Depends
from schemas import UserBase, UserDisplay
from db.database import get_db
from db import db_user
from sqlalchemy.orm import Session

router = APIRouter(prefix="/user", tags=["user"])


# Create
@router.post("/add", response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)


# Read all
@router.get("/read-users", response_model=List[UserDisplay])
def fetch_users(db: Session = Depends(get_db)):
    return db_user.fetch_users(db)


@router.get("/read-users/{user_id}", response_model=UserDisplay)
def get_one_user(user_id, db: Session = Depends(get_db)):
    user = db_user.get_user(db, user_id)
    if user:
        return user
    return {"error": f"No user with id {user_id}"}


# Update

# Delete