from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import schemas, models
from .database import SessionLocal

router = APIRouter()

# Зависимость для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Эндпоинт для создания пользователя
@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(username=user.username, email=user.email, hashed_password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Эндпоинт для получения пользователя по id
@router.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# Эндпоинт для создания инструмента
@router.post("/instruments/", response_model=schemas.Instrument)
def create_instrument(instrument: schemas.InstrumentCreate, db: Session = Depends(get_db)):
    db_instrument = models.Instrument(**instrument.dict())
    db.add(db_instrument)
    db.commit()
    db.refresh(db_instrument)
    return db_instrument

# Эндпоинт для получения инструмента по id
@router.get("/instruments/{instrument_id}", response_model=schemas.Instrument)
def read_instrument(instrument_id: int, db: Session = Depends(get_db)):
    db_instrument = db.query(models.Instrument).filter(models.Instrument.id == instrument_id).first()
    if db_instrument is None:
        raise HTTPException(status_code=404, detail="Instrument not found")
    return db_instrument

# Эндпоинт для создания заказа
@router.post("/orders/", response_model=schemas.Order)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    db_order = models.Order(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

# Эндпоинт для получения заказа по id
@router.get("/orders/{order_id}", response_model=schemas.Order)
def read_order(order_id: int, db: Session = Depends(get_db)):
    db_order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order


# Эндпоинт для удаления продукта
@router.delete("/instruments/{instrument_id}", response_model=schemas.Instrument)
def delete_instrument(instrument_id: int, db: Session = Depends(get_db)):
    db_instrument = db.query(models.Instrument).filter(models.Instrument.id == instrument_id).first()
    if db_instrument is None:
        raise HTTPException(status_code=404, detail="Instrument not found")
    db.delete(db_instrument)
    db.commit()
    return db_instrument

# Эндпоинт для редактирования продукта
@router.put("/instruments/{instrument_id}", response_model=schemas.Instrument)
def update_instrument(instrument_id: int, instrument: schemas.Instrument, db: Session = Depends(get_db)):
    db_instrument = db.query(models.Instrument).filter(models.Instrument.id == instrument_id).first()
    if db_instrument is None:
        raise HTTPException(status_code=404, detail="Instrument not found")
    for key, value in instrument.dict(exclude_unset=True).items():
        setattr(db_instrument, key, value)
    db.commit()
    db.refresh(db_instrument)
    return db_instrument