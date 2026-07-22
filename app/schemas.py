from pydantic import BaseModel


class ActivityBase(BaseModel):
    activity_number: str
    title: str
    tags: str = ""
    page_number: int
    analysis: str | None = None


class ActivityUpdate(BaseModel):
    activity_number: str | None = None
    title: str | None = None
    tags: str | None = None
    page_number: int | None = None
    analysis: str | None = None


class ActivityResponse(ActivityBase):
    id: int

    model_config = {"from_attributes": True}
