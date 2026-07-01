from typing import Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Activity
from app.schemas import ActivityUpdate

router = APIRouter(prefix="/api/activities", tags=["api"])


def _to_dict(a: Activity) -> dict:
    return {
        "id": a.id,
        "title": a.title,
        "tags": a.tags,
        "content": a.content,
        "page_number": a.page_number,
        "analysis": a.analysis,
        "created_at": a.created_at.isoformat() if a.created_at else None,
    }


@router.get("")
def list_activities(
    q: Optional[str] = None,
    tag: Optional[str] = None,
    db: Session = Depends(get_db),
):
    query = db.query(Activity)
    if q:
        query = query.filter(Activity.title.ilike(f"%{q}%"))
    if tag:
        query = query.filter(Activity.tags.ilike(f"%{tag}%"))
    return [_to_dict(a) for a in query.order_by(Activity.page_number).all()]


@router.get("/{activity_id}")
def get_activity(activity_id: int, db: Session = Depends(get_db)):
    a = db.query(Activity).filter(Activity.id == activity_id).first()
    if not a:
        raise HTTPException(404, "Atividade não encontrada")
    return _to_dict(a)


@router.put("/{activity_id}")
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
    return _to_dict(a)


@router.delete("/{activity_id}")
def delete_activity(activity_id: int, db: Session = Depends(get_db)):
    a = db.query(Activity).filter(Activity.id == activity_id).first()
    if not a:
        raise HTTPException(404, "Atividade não encontrada")
    db.delete(a)
    db.commit()
    return {"ok": True}
