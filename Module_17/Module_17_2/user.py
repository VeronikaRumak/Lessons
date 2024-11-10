from app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship


# В модуле user.py создайте модель User, наследованную от ранее написанного Base
# со следующими атрибутами:
class User(Base):
    # __tablename__ = 'users'
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    # id - целое число, первичный ключ, с индексом.
    id = Column(Integer, primary_key=True, index=True)
    # username - строка.
    username = Column(String)
    # firstname - строка.
    firstname = Column(String)
    # lastname - строка.
    lastname = Column(String)
    # age - целое число.
    age = Column(Integer)
    # slug - строка, уникальная, с индексом.
    slug = Column(String, unique=True, index=True)

    # tasks - объект связи с таблицей с таблицей Task, где back_populates='user'.
    tasks = relationship('Task', back_populates='user')


# from sqlalchemy.schema import CreateTable
# print(CreateTable(User.__table__))
