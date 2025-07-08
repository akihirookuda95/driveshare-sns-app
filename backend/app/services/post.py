from typing import List

from werkzeug.exceptions import NotFound
from sqlalchemy.exc import SQLAlchemyError

from backend.app.repositories.post import PostRepository
from backend.app.models.post import Post
from backend.app.schemas.post import PostCreateSchema, PostUpdateSchema, PostResponseSchema


class PostService:
    def __init__(self, repository: PostRepository):
        self.repository = repository


    def get_all_posts(self) -> List[Post]:
        """Retrieve all posts from the repository."""
        try:
            posts = self.repository.get_all_posts()
            return posts
        except SQLAlchemyError as e:
            raise Exception(f"Database error occured: {str(e)}")


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

    def create_post(self, post_data: dict) -> PostResponseSchema:
        """Create a new post in the repository."""

        # Validate input data
        post_schema = PostCreateSchema(**post_data)

        # Business Logic
        new_post = Post(
            title=post_schema.title,
            content=post_schema.content,
            user_id=post_schema.user_id,
        )
        new_post = self.repository.create_post(new_post)

        # Validate response data
        response = PostResponseSchema.model_validate(new_post)

        return response

    def update_post(self, post_id: int, post_data: dict) -> PostResponseSchema:
        """Update an existing post in the repository."""

        # Validate input data
        new_post: PostUpdateSchema = PostUpdateSchema(**post_data)

        # Business Logic
        original_post: Post = self.get_post_by_id(post_id)
        if new_post.title is not None:
            original_post.title = new_post.title
        if new_post.content is not None:
            original_post.content = new_post.content
        updated_post: Post = self.repository.update_post(original_post)

        # Validate response data
        response: PostResponseSchema = PostResponseSchema.model_validate(updated_post)

        return response


    def delete_post(self, post_id: int) -> None:
        """Delete a post from the repository."""
        post = self.get_post_by_id(post_id)
        self.repository.delete_post(post)

