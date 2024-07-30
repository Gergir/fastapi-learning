from sqlalchemy.orm.session import Session

from schemas import UserSchema
from db.models import DbUser
from db.hash import Hash
from fastapi import HTTPException, status

def create_user(db: Session, request: UserSchema):
    new_user = DbUser(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def fetch_users(db: Session):
    return db.query(DbUser).all()


def get_user(db: Session, user_id: int):
    user = db.query(DbUser).where(user_id == DbUser.id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {user_id} not found")
    return user


def update_user(db: Session, user_id: int, request: UserSchema):
    user = db.query(DbUser).where(user_id == DbUser.id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {user_id} not found")
    user.update({
        DbUser.username: request.username,
        DbUser.email: request.email,
        DbUser.password: Hash.bcrypt(request.password)
    })
    db.commit()
    return "OK"


def delete_user(db: Session, user_id: id):
    user = db.query(DbUser).where(user_id == DbUser.id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {user_id} not found")
    db.delete(user)
    db.commit()
    return f"user with {user_id} deleted"
