from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

class MessageBase(BaseModel):
    id: int = Field(..., description="The unique identifier of the message")
    sender_id: int = Field(..., description="The ID of the user who sent the message")
    receiver_id: int = Field(..., description="The ID of the user who received the message")
    content: str = Field(..., description="The content of the message")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="The timestamp when the message was created")
    is_read: bool = Field(default=False, description="Whether the message has been read")

    class Config:
        from_attributes = True


class MessageCreate(BaseModel):
    receiver_id: int = Field(..., description='The ID of the user who will receive the message')
    content: str = Field(..., min_length=1, max_length=1000, description='The content of the message')


class MessageUpdate(BaseModel):
    is_read: Optional[bool] = Field(None, description='Whether the message has been read')


class MessageListResponse(BaseModel):
    """メッセージ履歴のレスポンス"""
    messages: list[MessageBase] = Field(..., description='List of messages in the conversation')
    total: int = Field(..., description='Total number of messages in the conversation')
    page: int = Field(..., description='Current page number')
    per_page: int = Field(..., description='Number of messages per page')
