from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from src.database.api.routers.user_routers import get_users_by_statuses

jinja_router = APIRouter(
    prefix="/pages",
    tags=["Pages"]
)

templates = Jinja2Templates(directory="src/database/api/jinja/templates")


@jinja_router.get("/base")
def get_base_page(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})


@jinja_router.get("/search/{status}")
def get_search_page(request: Request, users=Depends(get_users_by_statuses)):
    return templates.TemplateResponse("search.html", {"request": request, "users": users["data"]})


@jinja_router.get("/chat")
def get_chat_page(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})
