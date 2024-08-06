
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated
from sqlalchemy import insert, select, update, delete


# Функция создания slug-строки
#from slugify import slugify

from backend.db_depends import get_db
from models.user import User
from models.task import Task
from schemas import CreateUser, UpdateUser


router = APIRouter(prefix="/user", tags=["user"])


@router.get("/")
async def all_users(db:  Annotated[Session, Depends(get_db)]):
    users = db.scalars(select(User)).all()
    return users



@router.get("/user_id")
async def user_by_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalar((select(User).where(User.id == user_id)))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found'
        )

    return user

@router.post("/create")
async def create_user(db:  Annotated[Session, Depends(get_db)], create_user: CreateUser):
    db.execute(insert(User).values(username = create_user.username,
                                   firstname = create_user.firstname,
                                   lastname = create_user.lastname,
                                   age = create_user.age))
    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful'
    }

@router.put("/update")
async def update_user(db:  Annotated[Session, Depends(get_db)], user_id: int, update_user: UpdateUser):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail='User was not found'
        )
    db.execute(update(User).where(User.id == user_id).values(
        username = update_user.username,
        firstname = update_user.firstname,
        lastname = update_user.lastname,
        age = update_user.age
    ))
    db.commit()
    return  {
                'status_code': status.HTTP_200_OK,
                'transaction': 'User update is successful!'
             }


@router.delete("/delete")
async def delete_user(db:  Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalar((select(User).where(User.id == user_id)))
    tasks = db.scalars((select(Task).where(Task.user_id == user_id)))
    if user is None:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail='User was not found'
        )
    if tasks is None:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail='Tasks of user was not found'
        )

    db.execute(delete(User).where(User.id == user_id))
    db.execute(delete(Task).where(Task.user_id == user_id))
    db.commit()
    return  {
                'status_code': status.HTTP_200_OK,
                'transaction': 'User delete is successful!'
             }

@router.get("/user_id/tasks")
async def tasks_by_user_id(db:  Annotated[Session, Depends(get_db)], user_id: int):
    tasks = db.scalars((select(Task).where(Task.id == user_id)))
    return tasks