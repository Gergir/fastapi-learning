from sqlalchemy.orm.session import Session
from db.models import DbArticle
from schemas import ArticleSchema
from exceptions import StoryException
from fastapi import HTTPException, status


def create_article(db: Session, request: ArticleSchema):
    if request.content.lower().startswith("once upon a time"):
        raise StoryException("No stories please")
    new_article = DbArticle(
        title=request.title,
        content=request.content,
        published=request.published,
        user_id=request.owner_id
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article


def get_article(db: Session, article_id: int):
    article = db.query(DbArticle).filter(article_id == DbArticle.id).first()
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Article with id {article_id} not found")
    return article
