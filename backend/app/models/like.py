from backend.app.extensions import db


class Like(db.Model):
    """
    投稿またはコメントに対する「いいね」を表すモデル
    """

    __tablename__ = 'likes'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=True)
    comment_id = db.Column(db.Integer, db.ForeignKey('comments.id'), nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    # 制約：post_id または comment_id のどちらか一方のみ設定可能
    __table_args__ = (
        # 同じユーザーが同じ投稿に複数回「いいね」できないようにする制約
        db.UniqueConstraint('user_id', 'post_id', name='unique_user_post_like'),

        # 同じユーザーが同じコメントに複数回「いいね」できないようにする制約
        db.UniqueConstraint('user_id', 'comment_id', name='unique_user_comment_like'),

        # 「いいね」は投稿かコメントのどちらか一方にのみ紐づく（両方には紐づかない）ことを保証する制約
        db.CheckConstraint(
            '(post_id IS NOT NULL AND comment_id IS NULL) OR (post_id IS NULL AND comment_id IS NOT NULL)',
            name='like_target_check'
        ),

        # indexを追加して検索性能を向上
        db.Index('idx_like_user_id', 'user_id'),
        db.Index('idx_like_post_id', 'post_id'),
        db.Index('idx_like_comment_id', 'comment_id'),
    )

    def __repr__(self):
        if self.post_id:
            return f'<Like {self.id} by User {self.user_id} on Post {self.post_id}>'
        else:
            return f'<Like {self.id} by User {self.user_id} on Comment {self.comment_id}>'

    def to_dict(self):
        """Convert the Like instance to a dictionary."""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'post_id': self.post_id,
            'comment_id': self.comment_id,
            'like_type': 'post' if self.post_id else 'comment' if self.comment_id else None,
            'created_at': self.created_at.isoformat() if self.created_at else None,
        }
