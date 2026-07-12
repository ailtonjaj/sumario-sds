import csv
import os
from app.database import SessionLocal
from app.models import Activity


def load_from_file(path: str = "sumario.csv"):
    if not os.path.exists(path):
        return

    db = SessionLocal()
    try:
        if db.query(Activity).count() > 0:
            return

        with open(path, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            count = 0
            for row in reader:
                if not row.get("título"):
                    continue
                db.add(
                    Activity(
                        activity_number=(row["número da atividade"]),
                        title=row["título"],
                        tags=row["tags"],
                        page_number=int(row["número da página"]),
                    )
                )
                count += 1
        db.commit()
        print(f"Importadas {count} atividades de {path}")
    finally:
        db.close()
