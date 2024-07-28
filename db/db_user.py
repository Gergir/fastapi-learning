from sqlalchemy.orm.session import Session

from schemas import UserBase
from db.models import DbUser
from db.hash import Hash


def create_user(db: Session, request: UserBase):
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
    return db.query(DbUser).where(user_id == DbUser.id).first()
