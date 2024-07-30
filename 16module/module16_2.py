from attr.validators import ge
from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get("/user/{user_id}")
async def news(user_id: Annotated[int, Path(ge = 1, le=100, description =
                                 'Enter User ID')]) -> dict:

    return{"message": f'привет {user_id}'}

@app.get('/user_new/{username}/{age}')
async def cap(username: Annotated[str,Path(min_length= 5, max_length=20,description='Enter username')],
              age: Annotated[int, Path(ge=18, le=120, description='Enter age')]) -> dict:
    return{"message": f'привет {username}, тебе {age} лет ' }
