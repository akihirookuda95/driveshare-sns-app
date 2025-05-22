from flask import Blueprint, jsonify, request

from backend.app.extensions import db
from backend.app.models.post import Post
from backend.app.schemas.post import PostCreate, PostBase


post_bp = Blueprint('post', __name__, url_prefix='/posts')


@post_bp.route('/', methods=['POST'])
def create_post():
    post_data = request.get_json()
    if not post_data:
        return jsonify({"error": "リクエストボディが空です。"}), 400
    post_schema = PostCreate(**post_data)

    new_post = Post(
        title=post_schema.title,
        content=post_schema.content,
        user_id=post_schema.user_id
    )

    db.session.add(new_post)
    db.session.commit()

    response = PostBase.model_validate(new_post)
    return jsonify(response.model_dump()), 201