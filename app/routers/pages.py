import os
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(tags=["frontend"])

templates_dir = os.path.join(
    os.path.dirname(__file__), "..", "..", "frontend", "templates"
)
templates = Jinja2Templates(directory=templates_dir)


@router.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(request, "index.html")


@router.get("/atividade/{activity_id}", response_class=HTMLResponse)
def atividade_page(request: Request, activity_id: int):
    return templates.TemplateResponse(
        request, "atividade.html", {"activity_id": activity_id}
    )
