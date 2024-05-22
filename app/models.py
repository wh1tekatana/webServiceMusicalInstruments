from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Instrument(Base):
    __tablename__ = 'instruments'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    brand = Column(String)
    type = Column(String)  # 1. Тип инструмента
    price = Column(Integer)  # 2. Цена
    stock = Column(Integer)  # 3. Количество на складе
    category = Column(String)  # 5. Категория
    manufacturer = Column(String)  # 6. Производитель

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    instrument_id = Column(Integer, ForeignKey('instruments.id'))
    quantity = Column(Integer)

    user = relationship('User', backref='orders')
    instrument = relationship('Instrument', backref='orders')
