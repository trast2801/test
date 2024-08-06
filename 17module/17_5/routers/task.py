import slugify
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from backend.db_depends import get_db
from typing import Annotated

from models.user import User
from models.task import Task

from sqlalchemy import insert
from schemas import CreateUser, CreateTask, UpdateTask
from sqlalchemy import select,update,delete


router = APIRouter(prefix="/task", tags=["task"])


@router.get("/")
async def all_tasks(db:  Annotated[Session, Depends(get_db)]):
    tasks = db.scalars(select(Task)).all()
    return tasks


@router.get("/task_id")

async def task_by_id(db: Annotated[Session, Depends(get_db)], task_id: int):
    task = db.scalar((select(Task).where(Task.id == task_id)))
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found'
        )

    return task

@router.post("/create")
async def create_task(db: Annotated[Session, Depends(get_db)], user_id: int, task_create_model: CreateTask):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is not None:
        db.execute(insert(Task).values(title=task_create_model.title,
                                       content=task_create_model.content,
                                       priority = task_create_model.priority,
                                       user_id=user.id,
                                       slug=task_create_model.title))
        db.commit()

        return {
            'status_code': status.HTTP_201_CREATED,
            'transaction': 'Successful'
        }

    raise HTTPException(
        status_code=404,
        detail="User was not found"
    )



@router.put("/update")
#async def update_task():
#    pass
async def update_task(db:  Annotated[Session, Depends(get_db)], task_id: int, update_task: UpdateTask):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail='User was not found'
        )
    db.execute(update(Task).where(task.id == task_id).values(
        title=update_task.title,
        content=update_task.content,
        priority=update_task.priority,
        #completed=create_task.comleted,
        slug=update_task.title,
    ))
    db.commit()
    return  {
                'status_code': status.HTTP_200_OK,
                'transaction': 'User update is successful!'
             }


@router.delete("/delete")
async def delete_task(db:  Annotated[Session, Depends(get_db)], task_id: int):
    task = db.scalar((select(User).where(Task.id == task_id)))
    if task is None:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail='User was not found'
        )
    db.execute(delete(Task).where(Task.id == task_id))
    db.commit()
    return  {
                'status_code': status.HTTP_200_OK,
                'transaction': 'Task delete is successful!'
             }