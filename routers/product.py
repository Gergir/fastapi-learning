from typing import List, Optional
from fastapi import APIRouter, Depends, Header, Cookie, Form
from fastapi.responses import Response, HTMLResponse, PlainTextResponse
from schemas import ArticleSchema, ArticleDisplay
from db.database import get_db
from db import db_article
from sqlalchemy.orm import Session

router = APIRouter(prefix="/product", tags=["product"])

products = ["banana", "milk", "cross"]


@router.get("/all")
def get_all_products():
    data = " ".join(products)
    response = Response(
        content=data,
        media_type="text/plain"
    )
    response.set_cookie(key="test_cookie", value="test_cookie_value")
    return response


@router.get("/with-header")
def get_product(
        response: Response,
        custom_header: Optional[List[str]] = Header(None),
        test_cookie_key: Optional[str] = Cookie(None)
):
    if custom_header:
        response.headers["custom_response_header"] = ", ".join(custom_header)
    return {
        "data": products,
        "custom_header": custom_header,
        "my_cookie": test_cookie_key
    }

@router.post("/new")
def create_post(name: str = Form(...)):
    products.append(name)
    return products


@router.get("/{product_id}", responses={
    200: {
        "content": {
            "text/html": {
                "example": "<div>Product</div>"
            }
        },
        "description": "Returns HTML for an object"
    },
    404: {
        "content": {
            "text/plain": {
                "example": "Product not available"
            }
        },
        "description": "A plain text message for an error message"
    }
})
def get_product(product_id: int):
    if product_id > len(products):
        out = "product not available"
        return PlainTextResponse(content=out, status_code=404)
    product = products[product_id]
    out = f"""
    <head>
        <style>
            .product {{
                bgcolor: "#232323";
                border: 1 solid red;
            }}
        </style>
    </head>
    <div class='product'>{product}</div>
    """
    return HTMLResponse(content=out)
