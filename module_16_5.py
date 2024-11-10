from fastapi import FastAPI, Path, HTTPException, status, Body, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import Annotated, List
from pydantic import BaseModel

app = FastAPI()

templates = Jinja2Templates(directory="templates")

# Создайте пустой список users = []
users = []


# Создайте класс(модель) User, наследованный от BaseModel,
# который будет содержать следующие поля:
# id - номер пользователя (int)
# username - имя пользователя (str)
# age - возраст пользователя (int)
class User(BaseModel):
    id: int
    username: str
    age: int


# Измените и дополните ранее описанные CRUD запросы:

# Напишите новый запрос по маршруту '/':
# Функция по этому запросу должна принимать аргумент request и возвращать TemplateResponse.
# TemplateResponse должен подключать ранее заготовленный шаблон 'users.html',
# а также передавать в него request и список users.
# Ключи в словаре для передачи определите самостоятельно в соответствии с шаблоном.
@app.get('/')
async def read(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('users.html', {"request": request, "users": users})


# get запрос по маршруту '/users' теперь возвращает список users.
@app.get('/users')
async def get_users() -> List[User]:
    return users


# Измените get запрос по маршруту '/user' на '/user/{user_id}':
# Функция по этому запросу теперь принимает аргумент request и user_id.
# Вместо возврата объекта модели User, теперь возвращается объект TemplateResponse.
# TemplateResponse должен подключать ранее заготовленный шаблон 'users.html',
# а также передавать в него request и одного из пользователей - user.
# Ключи в словаре для передачи определите самостоятельно в соответствии с шаблоном.
@app.get('/user/{user_id}')
async def read_user(request: Request,
                    user_id: Annotated[int, Path(description='Enter user ID', example=1)]):

    try:
        for user in users:
            if user.id == user_id:
                return templates.TemplateResponse("users.html", {"request": request, "user": user})

    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


# post запрос по маршруту '/user/{username}/{age}', теперь:
# Добавляет в список users объект User.
# id этого объекта будет на 1 больше, чем у последнего в списке users. Если список users пустой, то 1.
# Все остальные параметры объекта User - переданные в функцию username и age соответственно.
# В конце возвращает созданного пользователя.
@app.post('/user/{username}/{age}')
async def add_user(
        request: Request,
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=24)]) -> HTMLResponse:

    user_id = len(users) + 1
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)

    return templates.TemplateResponse("users.html", {"request": request, "user": users})


# put запрос по маршруту '/user/{user_id}/{username}/{age}', теперь:
# Обновляет username и age пользователя, если пользователь с таким user_id есть в списке users и возвращает его.
# В случае отсутствия пользователя выбрасывается исключение HTTPException с описанием "User was not found" и кодом 404.
@app.put('/user/{user_id}/{username}/{age}')
async def update_user(
        user_id: Annotated[int, Path(description='Enter user ID', example=1)],
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanProfi')],
        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=28)]) -> User:

    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
        else:
            raise HTTPException(status_code=404, detail="User was not found")


# delete запрос по маршруту '/user/{user_id}', теперь:
# Удаляет пользователя, если пользователь с таким user_id есть в списке users и возвращает его.
# В случае отсутствия пользователя выбрасывается исключение HTTPException с описанием "User was not found" и кодом 404.
@app.delete('/user/{user_id}')
async def delete_user(
        user_id: Annotated[int, Path(description='Enter user ID', example=2)]) -> User:
    try:
        for user in users:
            if user.id == user_id:
                users.pop(user_id)
                return user

    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")
