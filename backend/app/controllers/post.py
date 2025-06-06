import flask
from flask import Blueprint, jsonify, request

from backend.app.extensions import db
from backend.app.models.post import Post
from backend.app.repositories.post import PostRepository
from backend.app.schemas.post import PostCreateSchema, PostResponseSchema, PostUpdateSchema, PostDetail
from backend.app.services.post import PostService


post_bp = Blueprint('post', __name__, url_prefix='/posts')
post_service = PostService(repository=PostRepository())


@post_bp.route('/', methods=['GET'])
def get_all_posts() -> tuple[flask.Response, int]:
    """Retrieve all posts."""
    posts = post_service.get_all_posts()
    result = [PostResponseSchema.model_validate(post).model_dump() for post in posts]
    return jsonify(result), 200


@post_bp.route('/<int:post_id>', methods=['GET'])
def get_post_by_id(post_id: int) -> tuple[flask.Response, int]:
    """Retrieve a post by its ID."""
    post = post_service.get_post_by_id(post_id)
    result = PostResponseSchema.model_validate(post).model_dump()
    return jsonify(result), 200


@post_bp.route('/', methods=['POST'])
def create_post() -> tuple[flask.Response, int]:
    post_data = request.get_json()
    if not post_data:
        return jsonify({"error": "リクエストボディが空です。"}), 400

    post_schema = PostCreateSchema(**post_data)

    new_post = PostService.create_post(post_schema)

    response = PostResponseSchema.model_validate(new_post)
    return jsonify(response.model_dump()), 201


@post_bp.route('/<int:post_id>', methods=['PUT'])
def update_post(post_id: int) -> tuple[flask.Response, int]:
    post_data = request.get_json()
    if not post_data:
        return jsonify({"error": "リクエストボディが空です。"}), 400

    post_schema = PostCreateSchema(**post_data)

    updated_post = post_service.update_post(post_id, post_schema)

    response = PostUpdateSchema.model_validate(updated_post)
    return jsonify(response.model_dump()), 200

