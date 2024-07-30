from fastapi import FastAPI
from routers import users_get, users_post, user, article
from db import models
from db.database import engine

app = FastAPI()
app.include_router(user.router)
app.include_router(article.router)
app.include_router(users_get.router)
app.include_router(users_post.router)
@app.get("/")
def welcome():
    return {"message": "Hello there"}


models.Base.metadata.create_all(engine)
