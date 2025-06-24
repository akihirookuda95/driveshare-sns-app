from backend.app.extensions import db


class Follow(db.Model):
    """
    ユーザー間のフォロー関係を表すモデル
    """

    __tablename__ = 'follows'

    id = db.Column(db.Integer, primary_key=True)
    follower_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    followed_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    __table_args__ = (
        # 同じユーザー同士がフォローし合うことを防ぐためのユニーク制約
        db.UniqueConstraint('follower_id', 'followed_id', name='unique_follower_relationship'),
        # 自分自身をフォローできないようにするたねのチェック制約
        db.CheckConstraint('follower_id != followed_id', name='no_self_follow'),
    )

    def __repr__(self):
        return f'<Follow User {self.follower_id} follows User {self.followed_id}>'

    def to_dict(self):
        """Convert the Follow instance to a dictionary."""
        return {
            'id': self.id,
            'follower_id': self.follower_id,
            'followed_id': self.followed_id,
            'follower': {
                'id': self.follower.id,
                'username': self.follower.username,
            } if self.follower else None,
            'followed': {
                'id': self.followed.id,
                'username': self.followed.username,
            } if self.followed else None,
            'created_at': self.created_at.isoformat() if self.created_at else None,
        }
