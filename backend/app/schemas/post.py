from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class PostResponseSchema(BaseModel):
    id: int
    title: str
    content: str
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class PostCreateSchema(BaseModel):
    title: str
    content: str
    user_id: int


class PostUpdateSchema(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=100)
    content: Optional[str] = Field(None, min_length=1, max_length=255)


class PostDetail(PostResponseSchema):
    pass