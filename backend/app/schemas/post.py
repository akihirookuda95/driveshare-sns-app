from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, Field

from backend.app.schemas.user import UserBase
from backend.app.schemas.route import RouteBase


class PostResponseSchema(BaseModel):
    """Schema for post response."""
    id: int
    title: str
    content: str
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class PostListSchema(PostResponseSchema):
    """Schema for a list of posts."""
    # show only title, ID, user ID, and created_at
    content: Optional[str] = None # to avoid showing content in lists

    class Config:
        from_attributes = True


class PostDetailSchema(PostResponseSchema):
    """Schema for post detail response."""
    # includes user information if UserBase is defined
    user: Optional[UserBase] = None

    # includes related routes if RouteBase is defined
    routes: Optional[List[RouteBase]] = None

    class Config:
        from_attributes = True


class PostCreateSchema(BaseModel):
    title: str = Field(..., min_length=1, max_length=255, description="Title of the post")
    content: str = Field(..., min_length=1, max_length=1000, description="Content of the post")
    user_id: int = Field(..., description="ID of the user creating the post")


class PostUpdateSchema(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=255, description="Title of the post")
    content: Optional[str] = Field(None, min_length=1, max_length=1000, description="Content of the post")


class PaginatedResponse(BaseModel):
    """Schema for paginated response."""
    items: List[PostListSchema]
    total: int
    page: int
    per_page: int
    pages: int


    @classmethod
    def create(cls, items: List[PostListSchema], total: int, page: int, per_page: int) -> 'PaginatedResponse':
        """Create a paginated response."""
        pages = (total + per_page - 1) // per_page if per_page > 0 else 1
        return cls(
            items=[PostListSchema.model_validate(item).model_dump() for item in items],
            total=total,
            page=page,
            per_page=per_page,
            pages=pages
        )
