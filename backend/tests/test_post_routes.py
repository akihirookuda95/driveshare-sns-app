import pytest
from backend.app.models.post import Post

def test_create_post_success(test_client):
    payload = {
        "title": "テスト投稿",
        "content": "テスト内容",
        "user_id": 1
    }
    response = test_client.post("/posts/", json=payload)
    assert response.status_code == 201
    data = response.get_json()
    assert data["title"] == payload["title"]
    assert data["content"] == payload["content"]
    assert data["user_id"] == payload["user_id"]

def test_create_post_empty_body(test_client):
    response = test_client.post("/posts/", json=None)
    assert response.status_code == 400
    data = response.get_json()
    assert "リクエストボディが空です" in data["error"]

def test_create_post_missing_field(test_client):
    payload = {
        "content": "テスト内容",
        "user_id": 1
    }
    response = test_client.post("/posts/", json=payload)
    assert response.status_code == 400 or response.status_code == 422

def test_create_post_invalid_user_id(test_client):
    payload = {
        "title": "テスト投稿",
        "content": "テスト内容",
        "user_id": "abc"
    }
    response = test_client.post("/posts/", json=payload)
    assert response.status_code == 400 or response.status_code == 422
