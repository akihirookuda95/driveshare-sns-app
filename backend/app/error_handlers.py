import logging

from flask import jsonify
from werkzeug.exceptions import BadRequest
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from pydantic import ValidationError


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
        logging.error(f"Integrity error: {str(error)}")
        return jsonify({"error": "データベース整合性エラーが発生しました。"}), 409

    @app.errorhandler(SQLAlchemyError)
    def handle_sqlalchemy_error(error):
        logging.error(f"Database error: {str(error)}")
        return jsonify({"error": "データベースエラーが発生しました。"}), 500

    @app.errorhandler(Exception)
    def handle_exception(error):
        logging.error(f"Unexpected error: {str(error)}")
        return jsonify({"error": "予期しないエラーが発生しました。"}), 500