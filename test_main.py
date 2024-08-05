from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_all_users():
    response = client.get("/users/all")
    assert response.status_code == 200


def test_auth_error():
    response = client.post(
        "/token",
        data={
           "username": "",
           "password": ""
            })

    access_token = response.json().get("access_token")
    assert access_token is None
    message = response.json().get("detail")[0].get("msg")
    assert message == "Field required"


def test_auth_success():
    response = client.post(
        "/token",
        data={
            "username": "string",
            "password": "string"
        })

    access_token = response.json().get("access_token")
    assert access_token


def test_post_article():
    auth = client.post(
        "/token",
        data={
            "username": "string",
            "password": "string"
        })
    access_token = auth.json().get("access_token")

    assert access_token

    response = client.post(
        "/article/new",
        json={
            "title": "test title",
            "content": "test content",
            "published": False,
            "owner_id": 1
        },
        headers={
            "Authorization": "bearer " + access_token
        }
    )

    assert response.status_code == 200
    assert response.json().get("title") == "test title"
