from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from schemas import ProductSchema

router = APIRouter(prefix="/templates", tags=["templates"])


templates = Jinja2Templates(directory="templates")
@router.post("/products/{product_id}", response_class=HTMLResponse)
def get_product(product_id: str, product: ProductSchema, request: Request):
    return templates.TemplateResponse(
        "product.html",
        {
            "request": request,
            "product_id": product_id,
            "title": product.title,
            "description": product.description,
            "price": product.price
        }
    )
