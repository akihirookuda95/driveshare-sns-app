import flask
from flask import Blueprint, jsonify, request

from backend.app.schemas.message import MessageCreate, MessageBase, MessageListResponse
from backend.app.services.message import MessageService
from backend.app.repositories.message import MessageRepository


message_bp = Blueprint('message', __name__, url_prefix='/api/messages')
message_service = MessageService(repository=MessageRepository())


@message_bp.route('/', methods=['POST'])
def send_message():
    """
    メッセージ送信API
    POST /api/messages
    理由: フロントエンドからのメッセージ送信をバックエンドで永続化する
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
        message_data = MessageCreate(**data) # Validate and parse the request data
        # TODO: send_messageメソッドを実装する
        new_message = message_service.send_message(sender_id, message_data)
        response = MessageBase.model_validate(new_message) #
        return jsonify(response.model_dump()), 201 # model_dump() converts Pydantic model to dict
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@message_bp.route('/<int:user_id>/<int:recipient_id>', methods=['GET'])
def get_conversation(user_id: int, recipient_id: int) -> tuple[flask.Response, int]:
    """
    二人にユーザー間のメッセージ履歴取得
    GET /api/messages/<user_id>/<recipient_id>
    理由:フロントエンドでチャット履歴を表示するためのデータ取得
    """
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 50, type=int)

    try:
        # TODO: get_conversationメソッドを実装する
        messages, total = message_service.get_conversation(
            user_id, recipient_id, page=page, per_page=per_page
        )
        message_list = [MessageBase.model_validate(msg) for msg in messages]
        response = MessageListResponse(
            messages=message_list,
            total=total,
            page=page,
            per_page=per_page
        )
        return jsonify(response.model_dump()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

