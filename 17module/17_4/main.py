from fastapi import FastAPI
from routers import task, user

app = FastAPI()


@app.get("/")
async def welcome():
    return {"message": "Welcom to Taskmnager"}


app.include_router(user.router)
app.include_router(task.router)
