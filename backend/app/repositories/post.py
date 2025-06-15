from sqlite3 import IntegrityError
from typing import List, Optional, Any, Dict, Tuple

from sqlalchemy.exc import SQLAlchemyError

from backend.app.extensions import db
from backend.app.models.post import Post


class PostRepository:
    def __init__(self):
        self.db = db


    def get_all_posts(self) -> List[Post]:
        """Retrieve all posts from the database."""
        try:
            return Post.query.all()
        except SQLAlchemyError as e:
            raise Exception(f"Database getting error occured: {str(e)}")


    def get_post_by_id(self, post_id: int) -> Optional[Post]:
        """Retrieve a post by its ID."""
        try:
            return Post.query.get(post_id)
        except SQLAlchemyError as e:
            raise Exception(f"Database getting error occured: {str(e)}")


    def get_posts_with_filters(self, filters: Dict[str, Any], page: int = 1, per_page: int = 20) -> Tuple[List[Post], int]:
        """Retrieve posts with optional filters and pagination."""
        try:
            query = Post.query

            # apply filters
            if filters.get("title"):
                query = query.filter(Post.title.ilike(f"%{filters['title']}%"))
            if filters.get("user_id"):
                query = query.filter(Post.user_id == filters["user_id"])
            if filters.get("start_date"):
                query = query.filter(Post.created_at >= filters["start_date"])
            if filters.get("end_date"):
                query = query.filter(Post.created_at <= filters["end_date"])

            # get total count before pagination
            total = query.count()

            # apply pagination
            posts = query.offset((page - 1) * per_page).limit(per_page).all()

            return posts, total

        except SQLAlchemyError as e:
            raise Exception(f"Handle any SQLAlchemy errors: {str(e)}")


    def create_post(self, post: Post) -> Post:
        """Create a new post in the database."""
        try:
            self.db.session.add(post)
            self.db.session.commit()
            return post
        except IntegrityError:
            self.db.session.rollback()
            raise Exception(f"Database integrity error occured: Failed to create post.")
        except SQLAlchemyError:
            self.db.session.rollback()
            raise SQLAlchemyError(f"Database error occured: Failed to create post.")


    def update_post(self, post: Post) -> Post:
        """Update an existing post in the database."""
        try:
            self.db.session.merge(post)
            self.db.session.commit()
            return post
        except IntegrityError:
            self.db.session.rollback()
            raise Exception(f"Database integrity error occured: Failed to update post.")
        except SQLAlchemyError:
            self.db.session.rollback()
            raise Exception(f"Database error occured: Failed to update post.")


    def delete_post(self, post: Post) -> None:
        """Delete a post from the database."""
        try:
            self.db.session.delete(post)
            self.db.session.commit()
        except SQLAlchemyError as e:
            self.db.session.rollback()
            raise Exception(f"Database error occured: {str(e)}")
