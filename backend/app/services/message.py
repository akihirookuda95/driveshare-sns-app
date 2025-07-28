from backend.app.repositories.message import MessageRepository







class MessageService:
    def __init__(self, repository: MessageRepository):
        self.repository = repository

    # 新しいメッセージを投稿
    def post_message(self, message_data: str, user_id: int, recipinent_id: int):
        new_message = self.repository.create_message(message_data, user_id, recipinent_id)
