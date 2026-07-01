import json
import os
from app.database import SessionLocal
from app.models import Activity


def load_from_file(path: str = "atividades.json"):
    if not os.path.exists(path):
        return

    db = SessionLocal()
    try:
        if db.query(Activity).count() > 0:
            return

        with open(path, encoding="utf-8") as f:
            data = json.load(f)

        count = 0
        for item in data:
            tags = item.get("tags", "")
            if isinstance(tags, list):
                tags = ", ".join(tags)
            a = Activity(
                title=item["title"],
                tags=tags,
                content=item.get("content", ""),
                page_number=item.get("page", item.get("page_number", 0)),
                analysis=item.get("analysis"),
            )
            db.add(a)
            count += 1
        db.commit()
        print(f"Importadas {count} atividades de {path}")
    finally:
        db.close()
