from typing import List
from fastapi import APIRouter, Depends
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
    return Response(
        content=data,
        media_type="text/plain"
    )

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
