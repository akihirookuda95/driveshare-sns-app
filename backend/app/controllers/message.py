from flask import Blueprint, jsonify, request

from backend.app.repositories.message import MessageRepository
from backend.app.schemas.message import MessageCreate, MessageBase, MesssageListResponse


chat_bp = Blueprint('chat', __name__, url_prefix='/chats')
