from sqlalchemy.orm.session import Session

from schemas import UserSchema
from db.models import DbUser
from db.hash import Hash


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
    return db.query(DbUser).where(user_id == DbUser.id).first()


def update_user(db: Session, user_id: int, request: UserSchema):
    user = db.query(DbUser).filter(user_id == DbUser.id)
    user.update({
        DbUser.username: request.username,
        DbUser.email: request.email,
        DbUser.password: Hash.bcrypt(request.password)
    })
    db.commit()
    return "OK"


def delete_user(db: Session, user_id: id):
    user = db.query(DbUser).filter(user_id == DbUser.id).first()
    db.delete(user)
    db.commit()
    return f"user with {user_id} deleted"
