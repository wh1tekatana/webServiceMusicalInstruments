from pydantic import BaseModel
from typing import Optional

# Схема для создания пользователя
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

# Схема для чтения пользователя
class User(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        from_attributes = True

# Схема для обновления пользователя
class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    is_active: Optional[bool] = None

# Схема для создания инструмента
class InstrumentCreate(BaseModel):
    name: str
    description: Optional[str] = None
    brand: str
    type: str
    price: int
    stock: int
    category: str
    manufacturer: str

# Схема для чтения инструмента
class Instrument(InstrumentCreate):
    id: int

# Схема для обновления инструмента
class InstrumentUpdate(InstrumentCreate):
    pass

# Схема для создания заказа
class OrderCreate(BaseModel):
    user_id: int
    instrument_id: int
    quantity: int

# Схема для чтения заказа
class Order(OrderCreate):
    id: int

    class Config:
        from_attributes = True

# Добавьте другие схемы, если они есть