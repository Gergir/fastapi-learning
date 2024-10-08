from typing import List
from fastapi import APIRouter, Depends
from schemas import ArticleSchema, ArticleDisplay
from db.database import get_db
from db import db_article
from sqlalchemy.orm import Session
from auth.oauth2 import get_current_user
from schemas import UserSchema
router = APIRouter(prefix="/article", tags=["article"])


# create article
@router.post("/new", response_model=ArticleDisplay)
def create_article(
        request: ArticleSchema,
        db: Session = Depends(get_db),
        current_user: UserSchema = Depends(get_current_user)
                   ):
    return db_article.create_article(db, request)


# get article
@router.get("/{article_id}")#, response_model=ArticleDisplay)
def get_article(article_id: int, db: Session = Depends(get_db), current_user: UserSchema = Depends(get_current_user)):
    return {
        "data": db_article.get_article(db, article_id),
        "current_user": current_user
    }
    return db_article.get_article(db, article_id)