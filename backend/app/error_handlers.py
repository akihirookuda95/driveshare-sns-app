import logging

from flask import jsonify
from werkzeug.exceptions import BadRequest, NotFound
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from pydantic import ValidationError

from backend.app.extensions import db


def safe_rollback():
    """Safely rollback the database session."""
    try:
        db.session.rollback()
    except Exception as e:
        logging.error(f"Rollback failed: {str(e)}")
        try:
            db.session.close()
        except Exception:
            logging.critical("Failed to reset database session - application may be unstable.")

def register_error_handlers(app):

    @app.errorhandler(ValidationError)
    def handle_validation_error(error):
        logging.error(f"Validation error: {error.errors()}")
        return jsonify({"error": "入力内容に誤りがあります。"}), 422

    @app.errorhandler(BadRequest)
    def handle_bad_request(error):
        logging.error(f"Bad request: {error.description}")
        return jsonify({"error": "リクエストが不正です。"}), 400

    @app.errorhandler(IntegrityError)
    def handle_integrity_error(error):
        safe_rollback()
        logging.error(f"Integrity error: {str(error)}")
        return jsonify({"error": "データベース整合性エラーが発生しました。"}), 409

    @app.errorhandler(SQLAlchemyError)
    def handle_sqlalchemy_error(error):
        safe_rollback()
        logging.error(f"Database error: {str(error)}")
        return jsonify({"error": "データベースエラーが発生しました。"}), 500

    @app.errorhandler(Exception)
    def handle_exception(error):
        safe_rollback()
        logging.error(f"Unexpected error: {str(error)}")
        return jsonify({"error": "予期しないエラーが発生しました。"}), 500

    @app.errorhandler(NotFound)
    def handle_not_found(error):
        logging.error(f"Not found: {error.description}")
        return jsonify({"error": "リソースが見つかりません。"}), 404
