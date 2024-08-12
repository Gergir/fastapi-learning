from fastapi import APIRouter, Request, Depends
from custom_log import log
router = APIRouter(prefix="/dependencies", tags=["dependencies"],
                   dependencies=[Depends(log)])


def convert_params(request: Request, separator: str):
    query = []
    for key, value in request.query_params.items():
        query.append(f"{key} {separator} {value}")
        return query


def convert_header(request: Request, separator: str, query = Depends(convert_params)):
    out_headers = []
    for key, value in request.headers.items():
        out_headers.append(f"{key} {separator} {value}")
        return {
            "headers": out_headers,
            "query": query
        }


@router.get("/")
def get_items(separator: str = "-:-", headers=Depends(convert_header)):
    return {
        "items": ["a", "b", "c"],
        "headers": headers
    }


@router.post("/new")
def create_item(headers=Depends(convert_header)):
    return headers


class Account:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email


@router.post("/user")
def create_accoount(name: str, email: str, password: str, account: Account = Depends()):
    return {
        "name": account.name,
        "email": account.email,

    }
