from typing import List

from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import NotFound
from sqlalchemy.exc import SQLAlchemyError

from backend.app.repositories.post import PostRepository
from backend.app.models.post import Post
from backend.app.schemas.post import PostCreateSchema, PostUpdateSchema


class PostService:
    def __init__(self, repository: PostRepository):
        self.repository = repository

    def get_all_posts(self) -> List[Post]:
        """Retrieve all posts from the repository."""
        try:
            posts = self.repository.get_all_posts()
            if not posts:
                raise NotFound("No posts found.")
            return posts
        except SQLAlchemyError as e:
            raise Exception(f"Database error: {str(e)}")

    def get_post_by_id(self, post_id: int) -> Post:
        """Retrieve a post by its ID."""
        post = self.repository.get_post_by_id(post_id)
        if not post:
            raise NotFound(f"Post with ID {post_id} not found.")
        return post

    def get_posts_with_filters(self, filters: dict, page: int = 1, per_page: int = 20) -> tuple[List[Post], int]:
        """Retrieve posts with optional filters and pagination."""
        items, total = self.repository.get_posts_with_filters(filters, page, per_page)
        return items, total

    def create_post(self, post_data: PostCreateSchema) -> Post:
        """Create a new post in the repository."""
        new_post = Post(
            title=post_data.title,
            content=post_data.content,
            user_id=post_data.user_id,
        )
        return self.repository.create_post(new_post)

    def update_post(self, post_id: int, post_data: PostUpdateSchema) -> Post:
        """Update an existing post in the repository."""
        post = self.get_post_by_id(post_id)
        if post_data.title is not None:
            post.title = post_data.title
        if post_data.content is not None:
            post.content = post_data.content
        return self.repository.update_post(post)

    def delete_post(self, post_id: int) -> None:
        """Delete a post from the repository."""
        post = self.get_post_by_id(post_id)
        self.repository.delete_post(post)

