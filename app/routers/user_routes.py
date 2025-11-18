from fastapi import APIRouter, Depends, Request, Form
from sqlmodel import Session, select
from app.database import get_session
from app.models import CreateUser
from typing import Annotated
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse


router = APIRouter()
sessionDep = Annotated[Session, Depends(get_session)]

templates = Jinja2Templates(directory='app/templates')

@ router.get("/", response_class=HTMLResponse)
def register_form(request:Request):
    return templates.TemplateResponse("register.html",{"request": request})


@router.post('/register')
def register_user(session:sessionDep, name:str=Form(...), email:str = Form(...),phone:int=Form(...)):
    users = CreateUser(name=name, email=email, phone=phone)
    session.add(users)
    session.commit()
    return RedirectResponse(url = '/users', status_code =303)

@ router.get("/users", response_class=HTMLResponse)
def get_users(session:sessionDep, request:Request):
    users = session.exec(select(CreateUser)).all()
    return templates.TemplateResponse("users.html",{"request": request, "users":users})