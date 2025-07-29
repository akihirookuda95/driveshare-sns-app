from flask import Blueprint, jsonify, request
from networkx import expected_degree_graph
from sqlalchemy import true

from backend.app.schemas.message import MessageCreate, MessageBase, MesssageListResponse
from backend.app.services.message import MessageService
from backend.app.repositories.message import MessageRepository


message_bp = Blueprint('message', __name__, url_prefix='/api/messages')
message_service = MessageService(repository=MessageRepository())


@message_bp.route('/', methods=['POST'])
def send_message():
    """
    メッセージ送信API
    POST /api/messages
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "リクエストボディが空です。"}), 400

    # TODO: 実際のアプリではJWTトークンなどから取得
    # 現在は簡易的なリクエストボディから送信者IDを取得
    sender_id = data.get('sender_id')
    if not sender_id:
        return jsonify({"error": "送信者IDが必要です。"}), 400

    try:
        message_data = MessageCreate(**data)
        new_message = message_service.send_message(sender_id, message_data.)
        response = MessageBase.model_validate(new_message)
        return jsonify(response.model_dump()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
