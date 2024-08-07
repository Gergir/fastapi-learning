from fastapi import APIRouter, BackgroundTasks
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from schemas import ProductSchema
from custom_log import log

router = APIRouter(prefix="/templates", tags=["templates"])


templates = Jinja2Templates(directory="templates")
@router.post("/products/{product_id}", response_class=HTMLResponse)
def get_product(product_id: str, product: ProductSchema, request: Request, bt: BackgroundTasks):
    bt.add_task(log_template_call, f"Template for product added with id: {product_id}")
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


def log_template_call(message: str):
    log("MyAPI", message)