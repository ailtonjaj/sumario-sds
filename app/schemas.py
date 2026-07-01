from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ActivityBase(BaseModel):
    title: str
    tags: str = ""
    content: str = ""
    page_number: int
    analysis: Optional[str] = None


class ActivityCreate(ActivityBase):
    pass


class ActivityUpdate(BaseModel):
    title: Optional[str] = None
    tags: Optional[str] = None
    content: Optional[str] = None
    page_number: Optional[int] = None
    analysis: Optional[str] = None


class ActivityResponse(ActivityBase):
    id: int
    created_at: datetime

    model_config = {"from_attributes": True}
