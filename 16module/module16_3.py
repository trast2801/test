from fastapi import FastAPI

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}
@app.get("/users")
async  def get_users() -> dict:
    return users

@app.post("/user/{username}/{age}")
async def create_users(username:str, age : str ) -> dict:
    curnet_index = str(int(max(users,key=int)) + 1)
    users[curnet_index] = f'Имя: {username}, возраст: {age}'
    return f"User {curnet_index} is registered"

@app.put("'/user/{user_id}/{username}/{age}'")
async  def update_user(user_id : int, username: str, age : str):
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f"The user {user_id} is registered"

@app.delete("/user/{user_id}")
async def delete_user(user_id: int)->dict:
    users.pop(user_id)
    return f"User with {user_id} was delete"