
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def welcom():
    return "Главная страница"

@app.get("/user/admin")
async def welcom():
    return ("Вы вошли как администратор")
@app.get("/user/{user_id}")
async  def one(user_id):
    return (f'Вы вошли как пользователь № {user_id}')

@app.get("/user")
async def vsor(username : str, age : str):
    return (f"Информация о пользователе. Имя: {username}, Возраст:{age}")
