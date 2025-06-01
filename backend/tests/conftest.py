import pytest
from backend.app.main import create_app
from backend.app.extensions import db

@pytest.fixture
def test_client():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
    })

    with app.app_context():
        db.create_all()

        from backend.app.models.user import User
        user = User(id=1, username="testuser", email="test@example.com", password_hash="dummyhash")
        db.session.add(user)
        db.session.commit()

        yield app.test_client()
        db.session.remove()
        db.drop_all()