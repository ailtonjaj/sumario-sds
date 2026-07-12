from typing import Optional
from pydantic import BaseModel


class ActivityBase(BaseModel):
    activity_number: str
    title: str
    tags: str = ""
    page_number: int
    analysis: Optional[str] = None


class ActivityUpdate(BaseModel):
    activity_number: Optional[str] = None
    title: Optional[str] = None
    tags: Optional[str] = None
    page_number: Optional[int] = None
    analysis: Optional[str] = None


class ActivityResponse(ActivityBase):
    id: int

    model_config = {"from_attributes": True}
