from typing import List
from pydantic import BaseModel


# Article inside UserDisplay
class Article(BaseModel):
    title: str
    content: str
    published: bool

    class Config:
        orm_mode = True


class UserSchema(BaseModel):
    username: str
    email: str
    password: str


class UserDisplay(BaseModel):
    username: str
    email: str
    items: List[Article] = []

    class Config:
        orm_mode = True


class ArticleSchema(BaseModel):
    title: str
    content: str
    published: bool
    owner_id: int


# User inside article display
class User(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True


class ArticleDisplay(BaseModel):
    title: str
    content: str
    published: bool
    user: User

    class Config:
        orm_mode = True


class ProductSchema(BaseModel):
    title: str
    description: str
    price: float
