from backend.app.extensions import db


class Post(db.Model):
    """
    投稿を表すモデル
    """

    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    comments = db.relationship('Comment', backref='post', lazy=True, cascade='all, delete-orphan')
    routes = db.relationship('Route', backref='post', lazy=True, cascade='all, delete-orphan')
    likes = db.relationship('Like', foreign_keys='Like.post_id', backref='post', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Post {self.title}>'

    def to_dict(self, include_relationships=True):
        """Convert the Post instance to a dictionary.

        Args:
            include_relationships (bool): If True, include comments and routes.
                                          Default is True.
        """
        result = {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'user_id': self.user_id,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
        }

        if include_relationships:
            result.update({
                'comments': [comment.to_dict(include_relationships=False) for comment in self.comments],
                'routes': [route.to_dict(include_relationships=False) for route in self.routes],
            })

        return result
