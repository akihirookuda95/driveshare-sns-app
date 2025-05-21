from datetime import datetime

from pydantic import BaseModel


class PostBase(BaseModel):
    id: int
    title: str
    content: str
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class PostCreate(BaseModel):
    title: str
    content: str
    user_id: int