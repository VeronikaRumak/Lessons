from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import Column, Integer, String

# В модуле db.py:
# Импортируйте все необходимые функции и классы,

# создайте движок указав пусть в БД - 'sqlite:///taskmanager.db' и
engine = create_engine("sqlite:///taskmanager.db", echo=True)

# локальную сессию (по аналогии с видео лекцией).
SessionLocal = sessionmaker(bind=engine)


# Создайте базовый класс Base для других моделей, наследуясь от DeclarativeBase.
class Base(DeclarativeBase):
    pass


