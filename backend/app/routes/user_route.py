import logging
-from sqlite3 import IntegrityError
+from sqlalchemy.exc import IntegrityError

from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError

from backend.app.extensions import db
from backend.app.models.user import User
from backend.app.schemas.user import UserBase, UserCreate


user_bp = Blueprint('user', __name__)
logger = logging.getLogger(__name__)


@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()

    try:
        user_data = UserCreate(**data)
        new_user = User(
            username=user_data.username,
            email=user_data.email,
            password_hash=user_data.password,  # TODO: Ensure to hash the password in a real application
        )
        db.session.add(new_user)
        db.session.commit()
        response = UserBase.model_validate(new_user)
        return jsonify(response.model_dump()), 201

    except ValidationError as e:
        logger.warning(f"Validation error: {e.errors()}")
        return jsonify({"error": "入力内容に誤りがあります。"}), 400

    except IntegrityError as e:
        db.session.rollback()
        logger.warning(f"Integrity error: {str(e)}")
        return jsonify({"error": "このメールアドレスは既に登録されています。"}), 409

    except SQLAlchemyError as e:
        db.session.rollback()
        logger.error(f"Database error: {str(e)}")
        return jsonify({"error": "サーバー内部でエラーが発生しました。"}), 500

    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return jsonify({"error": "予期しないエラーが発生しました。"}), 500