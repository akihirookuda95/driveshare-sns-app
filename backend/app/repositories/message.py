
from backend.app.extensions import db

class MessageRepository:
    def __init__(self):
        self.db = db

    # 新しいメッセージを作成
    def create_message(self, message_data: str, user_id: int, recipient_id: int):
        pass


    # 二人のユーザー間のメッセージ履歴を取得
    def get_messages_between_users(self, user_id: int, recipient_id: int):
        pass
