from fastapi import APIRouter, Request, Depends

router = APIRouter(prefix="/dependencies", tags=["dependencies"])


def convert_header(request: Request)
    out_headers = []
    for key, value in request.headers.items():
        out_headers.append(f"{key}: {value}")
        return out_headers


@router.get("/")
def get_items(headers=Depends(convert_header)):
    return {
        "items": ["a", "b", "c"],
        "headers": headers
    }


@router.post("/new")
def create_item(headers=Depends(convert_header)):
    return headers

