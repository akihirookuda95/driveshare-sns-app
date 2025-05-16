from datetime import datetime

from pydantic import BaseModel


class RouteBase(BaseModel):
    id: int
    post_id: int
    start_location: str
    end_location: str
    distance: float
    duration: float
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class RouteCreate(BaseModel):
    post_id: int
    start_location: str
    end_location: str
    distance: float
    duration: float
