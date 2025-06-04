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


def test_get_post_detail_success(test_client):
    # First, create a post
    payload = {
        "title": "テスト投稿",
        "content": "テスト内容",
        "user_id": 1
    }

    create_response = test_client.post("/posts/", json=payload)
    post_id = create_response.get_json()["id"]

    # Now get the post details
    response = test_client.get(f"/posts/{post_id}")
    assert response.status_code == 200
    data = response.get_json()
    assert data["title"] == payload["title"]
    assert data["content"] == payload["content"]
    assert data["user_id"] == payload["user_id"]
    assert "created_at" in data
    assert "updated_at" in data


def test_get_post_detail_not_found(test_client):
    # Use a non-existent post ID
    response = test_client.get("/posts/9999")
    assert response.status_code == 404
    data = response.get_json()
    assert "Post with ID 9999 not found." in data["error"]