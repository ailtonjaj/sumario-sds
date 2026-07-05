from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    tags = Column(String, default="")
    page_number = Column(Integer, nullable=False)
    analysis = Column(Text, nullable=True, default=None)
