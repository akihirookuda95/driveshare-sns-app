from backend.app.extensions import db


class Message(db.Model):
    """"DMメッセージモデル"""

    __tablename__ =  'messages'

    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    is_read = db.Column(db.Boolean, default=False, nullable=False)

    sender = db.relationship('User', foreign_keys=[sender_id])
    receiver = db.relationship('User', foreign_keys=[receiver_id])

    __table_args__ = (
        db.Index('idx_message_sender_receiver', 'sender_id', 'receiver_id'),
        db.Index('idx_message_created_at', 'created_at'),
        db.CheckConstraint('sender_id != receiver_id', name='no_self_message'),
    )

    def __repr__(selfl):
        return f'<Message {self.id} from {self.sender_id} to User {self.receiver_id}>'

    def to_dict(self):
        """Convert the Message to a dictionary."""
        return {
            'id': self.id,
            'sender_id': self.sender_id,
            'receiver_id': self.receiver_id,
            'content': self.content,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'is_read': self.is_read
        }
