

import uvicorn
from fastapi import FastAPI, status, Body, HTTPException, Path
from pydantic import BaseModel
from typing import List

app = FastAPI()
users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int = None


@app.get("/users")
async def get_users() -> List[User]:
    global users
    return users


# Создание пользователя
@app.post("/user/{username}/{age}")
async def create_user(username: str, age: int):
    global users
    new_user = User(id=len(users) + 1, username=username, age=age)
    users.append(new_user)
    return new_user
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
async def delete_user(user_id: int = Path(...)):
    global users
    user = next((u for u in users if u.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")
    users.remove(user)
    return user

'''

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
'''