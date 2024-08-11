from fastapi import FastAPI
from routers import users_get, users_post, user, article, product, file, dependency
from auth import authentication
from db import models
from db.database import engine
from exceptions import StoryException
from fastapi import Request, status, HTTPException
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from templates import templates
from fastapi.responses import HTMLResponse
import time
from client import html
from fastapi.websockets import WebSocket

app = FastAPI()
app.include_router(templates.router)
app.include_router(authentication.router)
app.include_router(product.router)
app.include_router(user.router)
app.include_router(article.router)
app.include_router(file.router)
app.include_router(users_get.router)
app.include_router(dependency.router)
# app.include_router(users_post.router)


# @app.get("/")
# def welcome():
#     return {"message": "Hello there"}


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

@app.middleware("http")
async def add_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    response.headers['duration'] = str(duration)
    return response


@app.get("/")
async def get():
    return HTMLResponse(html)

clients = []
@app.websocket("/chat")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    while True:
        data = await websocket.receive_text()
        for client in clients:
            await client.send_text(data)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.mount("/files",
          StaticFiles(directory="files"),
          name="files"
          )

app.mount("/templates/static",
          StaticFiles(directory="templates/static"),
          name="static"
          )
