import os
import time
from pathlib import Path
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from app.models import Base

DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///./sumario.db")

_is_sqlite = DATABASE_URL.startswith("sqlite")

if _is_sqlite:
    _db_path = DATABASE_URL.removeprefix("sqlite:///")
    Path(_db_path).parent.mkdir(parents=True, exist_ok=True)
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
else:
    engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    Base.metadata.create_all(bind=engine)


def wait_for_db(max_retries=15, delay=2):
    for attempt in range(max_retries):
        try:
            with engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            return
        except Exception:
            if attempt < max_retries - 1:
                time.sleep(delay)
    raise RuntimeError("Could not connect to database after retries")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
