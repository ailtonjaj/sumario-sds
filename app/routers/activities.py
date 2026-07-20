from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import and_
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Activity
from app.schemas import ActivityUpdate, ActivityResponse

router = APIRouter(prefix="/api/activities", tags=["api"])


@router.get("", response_model=list[ActivityResponse])
def list_activities(
    search_term: Optional[str] = None,
    tag: Optional[list[str]] = Query(default=None),
    status: Optional[str] = None,
    db: Session = Depends(get_db),
):
    query = db.query(Activity)
    if search_term:
        query = query.filter(Activity.title.ilike(f"%{search_term}%"))
    if tag:
        query = query.filter(and_(*[Activity.tags.ilike(f"%{t}%") for t in tag]))
    if status == "done":
        query = query.filter(Activity.analysis != None, Activity.analysis != "")
    elif status == "pending":
        query = query.filter((Activity.analysis == None) | (Activity.analysis == ""))
    return query.order_by(Activity.page_number, Activity.activity_number).all()


@router.get("/{activity_id}", response_model=ActivityResponse)
def get_activity(activity_id: int, db: Session = Depends(get_db)):
    a = db.query(Activity).filter(Activity.id == activity_id).first()
    if not a:
        raise HTTPException(404, "Atividade não encontrada")
    return a


@router.put("/{activity_id}", response_model=ActivityResponse)
def update_activity(
    activity_id: int,
    data: ActivityUpdate,
    db: Session = Depends(get_db),
):
    a = db.query(Activity).filter(Activity.id == activity_id).first()
    if not a:
        raise HTTPException(404, "Atividade não encontrada")
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(a, field, value)
    db.commit()
    db.refresh(a)
    return a
