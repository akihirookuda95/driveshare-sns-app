from typing import List, Optional, Any, Dict

from sqlalchemy.exc import SQLAlchemyError

from backend.app.extensions import db
from backend.app.models.post import Post


class PostRepository:
    @staticmethod
    def get_all_posts() -> List[Post]:
        """Retrieve all posts from the database."""
        return Post.query.all()

    @staticmethod
    def get_post_by_id(post_id: int) -> Optional[Post]:
        """Retrieve a post by its ID."""
        return Post.query.get(post_id)

    @staticmethod
    def get_posts_with_filters(filters: Dict[str, Any], page: int = 1, per_page: int = 20) -> (List[Post], int):
        """Retrieve posts with optional filters and pagination."""
        query = Post.query
        if filters.get('title'):
            query = query.filter(Post.title.ilike(f'%{filters["title"]}%'))

        paginated = query.paginate(page=page, per_page=per_page)
        return paginated.items, paginated.total

    @staticmethod
    def create_post(post: Post) -> Post:
        """Create a new post in the database."""
        try:
            db.session.add(post)
            db.session.commit()
            return post
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e

    @staticmethod
    def update_post(post: Post) -> Post:
        """Update an existing post in the database."""
        try:
            db.session.add(post)
            db.session.commit()
            return post
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e

    @staticmethod
    def delete_post(post: Post) -> None:
        """Delete a post from the database."""
        try:
            db.session.delete(post)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e

    @staticmethod
    def begin_transaction() -> None:
        """Begin a new database transaction."""
        pass

    @staticmethod
    def commit_transaction() -> None:
        """Commit the current database transaction."""
        try:
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e

    @staticmethod
    def rollback_transaction() -> None:
        """Rollback the current database transaction."""
        db.session.rollback()