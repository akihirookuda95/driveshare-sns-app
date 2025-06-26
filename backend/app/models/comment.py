from backend.app.extensions import db


class Comment(db.Model):
    """
    投稿に対するコメントを表すモデル
    """

    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    likes = db.relationship('Like', foreign_keys='Like.comment_id', backref='comment', lazy=True, cascade='all, delete-orphan')

    __table_args__ = (
        db.Index('idx_post_created', 'post_id', 'created_at'),
    )

    def __repr__(self):
        return f'<Comment {self.id} by User {self.user_id} on Post {self.post_id}>'

    def to_dict(self):
        """Convert the Comment instance to a dictionary."""

        return {
            'id': self.id,
            'content': self.content,
            'user_id': self.user_id,
            'post_id': self.post_id,
            'user': {
                'id': self.author.id,
                'username': self.author.username,
            } if self.author else None,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
        }
