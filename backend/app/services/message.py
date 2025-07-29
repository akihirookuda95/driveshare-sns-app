from backend.app.repositories.message import MessageRepository







class MessageService:
    def __init__(self, repository: MessageRepository):
        self.repository = repository

    # 新しいメッセージを投稿
    def send_message(self, user_id: int, message_data: str):
        new_message = self.repository.create_message(sender_id, message_data)
        return new_message
