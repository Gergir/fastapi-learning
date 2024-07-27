from fastapi import FastAPI
from routers import users_get, users_post

app = FastAPI()
app.include_router(users_get.router)
app.include_router(users_post.router)


@app.get("/")
def welcome():
    return {"message": "Hello there"}


