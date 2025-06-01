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
    response = test_client.post("/posts/", data=None, content_type="application/json")
    assert response.status_code == 400
    data = response.get_json()
    assert "リクエストが不正です。" in data["error"]


def test_create_post_missing_field(test_client):
    payload = {
        "title": "テスト投稿",
        "user_id": 1
    }
    response = test_client.post("/posts/", json=payload)
    assert response.status_code == 422
    data = response.get_json()
    assert "入力内容に誤りがあります。" in data["error"]


def test_create_post_invalid_title(test_client):
    payload = {
        "title": 12345,
        "content": "テスト内容",
        "user_id": 1
    }
    response = test_client.post("/posts/", json=payload)
    assert response.status_code == 422
    data = response.get_json()
    assert "入力内容に誤りがあります。" in data["error"]