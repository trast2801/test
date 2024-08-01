
from fastapi import FastAPI, status, Body, HTTPException, Request, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List
from fastapi.templating import Jinja2Templates
from pygments.lexers import templates


app = FastAPI()
users = []

templates = Jinja2Templates(directory='templates')

class User(BaseModel):
    id: int = None
    username: str
    age: int = None


@app.get("/")
async  def get_all_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse ("users.html", {"request": request, "users": users})

@app.get(path="/user/{user_id}")
async def get_user(request: Request, user_id: int) -> HTMLResponse:
    return templates.TemplateResponse("users.html",{"request": request, "user": users[user_id]})

# Создание пользователя
@app.post("/user/{username}/{age}")
async def create_user(username: str, age: int):
    global users
    if len(users):
        new_user = User(id=len(users), username=username, age=age)
    else:
        new_user = User(id=0, username=username, age=age)
    users.append(new_user)
    return new_user

# Обновление пользователя
@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int , username: str, age: int):
    global users
    user = next((u for u in users if u.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")
    user.username = username
    user.age = age
    return user

@app.delete("/user/{user_id}")
async def delete_user(user_id: int):
    global users
    user = next((u for u in users if u.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")
    users.remove(user)
    return user

