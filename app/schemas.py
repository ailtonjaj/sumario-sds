from typing import Optional
from pydantic import BaseModel


class ActivityBase(BaseModel):
    title: str
    tags: str = ""
    page_number: int
    analysis: Optional[str] = None


class ActivityUpdate(BaseModel):
    title: Optional[str] = None
    tags: Optional[str] = None
    page_number: Optional[int] = None
    analysis: Optional[str] = None


class ActivityResponse(ActivityBase):
    id: int

    model_config = {"from_attributes": True}
