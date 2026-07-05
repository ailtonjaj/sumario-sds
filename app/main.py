from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.database import init_db, wait_for_db
from app.import_data import load_from_file
from app.routers.activities import router as activities_router
from app.routers.pages import router as pages_router

app = FastAPI(title="Sumário - 365 Atividades STEM")

app.mount("/static", StaticFiles(directory="frontend/static"), name="static")
app.include_router(activities_router)
app.include_router(pages_router)


@app.on_event("startup")
def on_startup():
    wait_for_db()
    init_db()
    load_from_file()
