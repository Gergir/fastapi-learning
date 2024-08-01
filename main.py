from fastapi import FastAPI
from routers import users_get, users_post, user, article, product
from db import models
from db.database import engine
from exceptions import StoryException
from fastapi import Request, status, HTTPException
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.include_router(product.router)
app.include_router(user.router)
app.include_router(article.router)
# app.include_router(users_get.router)
# app.include_router(users_post.router)


@app.get("/")
def welcome():
    return {"message": "Hello there"}


@app.exception_handler(StoryException)
def handle_story_exceptions(request: Request, exception: StoryException):
    return JSONResponse(
        status_code=status.HTTP_408_REQUEST_TIMEOUT,
        content={"detail": exception.name}
    )
# @app.exception_handler(HTTPException)
# def handle_custom_exceptions(request: Request, exception: Exception):
#     return PlainTextResponse(str(exception), 400)


models.Base.metadata.create_all(engine)

origins = [
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
