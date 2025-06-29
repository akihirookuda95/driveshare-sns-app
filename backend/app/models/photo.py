from backend.app.extensions import db


class Photo(db.Model):
    """
    投稿に関連する画像を表すモデル
    """

    __tablename__ = 'photos'

    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    caption = db.Column(db.String(500), nullable=True)
    display_order = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return f'<PostImage {self.id} for Post {self.post_id}>'

    def to_dict(self):
        """Convert the PostImage instance to a dictionary."""
        return {
            'id': self.id,
            'post_id': self.post_id,
            'image_url': self.image_url,
            'caption': self.caption,
            'display_order': self.display_order,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
