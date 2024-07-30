from sqlalchemy.orm.session import Session
from db.models import DbArticle
from schemas import ArticleSchema


def create_article(db: Session, request: ArticleSchema):
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
    return article
