from app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.models import *


# В модуле task.py создайте модель Task, наследованную от ранее написанного Base
# со следующими атрибутами:
class Task(Base):
    # __tablename__ = 'tasks'
    __tablename__ = 'tasks'
    __table_args__ = {'extend_existing': True}
    # id - целое число, первичный ключ, с индексом.
    id = Column(Integer, primary_key=True, index=True)
    # title - строка.
    title = Column(String)
    # content - строка.
    content = Column(String)
    # priority - целое число, по умолчанию 0.
    priority = Column(Integer, default=0)
    # completed - булевое значение, по умолчанию False.
    completed = Column(Boolean, default=False)
    # user_id - целое число, внешний ключ на id из таблицы 'users', не NULL, с индексом.
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False, index=True)
    # slug - строка, уникальная, с индексом.
    slug = Column(String, unique=True, index=True)

    # user - объект связи с таблицей с таблицей User, где back_populates='tasks'.
    user = relationship('User', back_populates='tasks')


#from sqlalchemy.schema import CreateTable
#print(CreateTable(Task.__table__))
#print(CreateTable(User.__table__))
