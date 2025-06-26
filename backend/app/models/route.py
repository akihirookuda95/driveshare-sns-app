from backend.app.extensions import db


class Route(db.Model):
    """
    投稿に関連するルート情報を表すモデル
    """

    __tablename__ = 'routes'

    id = db.Column(db.Integer, primary_key=True)
    start_location = db.Column(db.String(255), nullable=False)
    end_location = db.Column(db.String(255), nullable=False)
    distance = db.Column(db.Float, nullable=False)
    duration = db.Column(db.Float, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    difficulty_level = db.Column(db.Integer, nullable=True) # 1. 初級者向け, 2. 中級者向け, 3. 上級者向け
    curve_count = db.Column(db.Integer, nullable=True) # カーブの数
    elevation_change = db.Column(db.Integer, nullable=True) # 標高差（メートル）
    road_condition = db.Column(db.String(100), nullable=True) # 道路の状態（例: 良好, 悪い, 未舗装など）
    traffic_level = db.Column(db.Integer, nullable=True) # 交通量レベル（1. 低, 2. 中, 3. 高）
    difficulty_notes = db.Column(db.Text, nullable=True) # 難易度に関するメモや説明
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    __table_args__ = (
        db.Index('idx_route_difficulty_level', 'difficulty_level'),
        db.Index('idx_route_post_id', 'post_id'),
    )

    def __repr__(self):
        return f'<Route {self.start_location} to {self.end_location}>'

    def to_dict(self):
        """Convert the Route instance to a dictionary."""

        return {
            'id': self.id,
            'start_location': self.start_location,
            'end_location': self.end_location,
            'distance': self.distance,
            'duration': self.duration,
            'post_id': self.post_id,
            'difficulty_level': self.difficulty_level,
            'curve_count': self.curve_count,
            'elevation_change': self.elevation_change,
            'road_condition': self.road_condition,
            'traffic_level': self.traffic_level,
            'difficulty_notes': self.difficulty_notes,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
        }

    def get_difficulty_display(self):
        """Return a user-friendly display of the difficulty level."""
        difficulty_map = {
            1: '初級者向け',
            2: '中級者向け',
            3: '上級者向け'
        }
        return difficulty_map.get(self.difficulty_level, '未設定')
