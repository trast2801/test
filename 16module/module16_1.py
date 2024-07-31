

from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/")
async def head_page():
    return "Главная страница"

@app.get("/user/admin")
async def admin_enter():
    return ("Вы вошли как администратор")
@app.get("/user/{user_id}")
async  def user_enter(user_id):
    return (f'Вы вошли как пользователь № {user_id}')

@app.get("/user")
async def info_about_user(username : str, age : int):
    return (f"Информация о пользователе. Имя: {username}, Возраст:{age}")

@app.get("/user/{username}")
async def user_name(username : str = Path(min_length = 3, max_length=15, description =
                                "Введите ваше имя ")) -> dict:

    return{"message": f'привет {username} {id}'}

