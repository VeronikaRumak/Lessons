from fastapi import APIRouter, Depends, status, HTTPException
# Сессия БД
from sqlalchemy.orm import Session
# Функция подключения к БД
from app.backend.db_depends import get_db
# Аннотации, Модели БД и Pydantic.
from typing import Annotated
from app.models import Task, User
from app.schemas import CreateTask, UpdateTask
# Функции работы с записями.
from sqlalchemy import insert, select, update, delete
# Функция создания slug-строки
from slugify import slugify


# В модуле task.py напишите APIRouter с префиксом '/task' и тегом 'task',
# а также следующие маршруты, с пустыми функциями:
router = APIRouter(prefix='/task', tags=['task'])


# Функция all_tasks ('/') - идентично all_users.
@router.get('/')
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    tasks = db.scalars(select(Task)).all()
    return tasks


# Функция task_by_id ('/task_id') - идентично user_by_id.
@router.get('/task_id')
async def task_by_id(task_id: int,
                     db: Annotated[Session, Depends(get_db)]):

    task = db.scalars(select(Task).where(Task.id == task_id)).first()

    if task:
        return task

    else:
        raise HTTPException(status_code=404, detail="Task was not found")


# Функция craete_task ('/create'):
# Дополнительно принимает модель CreateTask и user_id.
# Подставляет в таблицу Task запись значениями указанными в CreateUser и user_id,
# если пользователь найден.
# Т.е. при создании записи Task вам необходимо связать её с конкретным пользователем User.
# В конце возвращает словарь {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}
# В случае отсутствия пользователя выбрасывает исключение с кодом 404 и описанием "User was not found"
@router.post('/create')
async def create_task(user_id: int,
                      db: Annotated[Session, Depends(get_db)],
                      create_task: CreateTask):

    user = db.scalars(select(User).where(User.id == user_id))

    if user:
        db.execute(insert(Task).values(
            title=create_task.title,
            content=create_task.content,
            priority=create_task.priority,
            user_id=user_id,
            slug=slugify(create_task.title)
        ))
        db.commit()
        return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}

    else:
        raise HTTPException(status_code=404, detail="User was not found")


# Функция update_task ('/update') - идентично update_user.
@router.put('/update')
async def update_task(task_id: int,
                      db: Annotated[Session, Depends(get_db)],
                      update_task: UpdateTask):

    task = db.scalar(select(Task).where(Task.id == task_id))

    if task is not None:
        db.execute(update(Task).where(Task.id == task_id).values(
            title=update_task.title,
            content=update_task.content,
            priority=update_task.priority
        ))
        db.commit()
        return {'status_code': status.HTTP_200_OK, 'transaction': 'Task update is successful!'}

    raise HTTPException(status_code=404, detail="Task was not found")


# Функция delete_task ('/delete') - идентично delete_user.
@router.delete('/delete')
async def delete_task(task_id: int,
                      db: Annotated[Session, Depends(get_db)]):

    task = db.scalar(select(Task).where(Task.id == task_id))

    if task:
        db.execute(delete(Task).where(Task.id == task_id))
        db.commit()
        return {'status_code': status.HTTP_200_OK, 'transaction': 'Task deleted successfully!'}

    else:
        raise HTTPException(status_code=404, detail="Task was not found")


