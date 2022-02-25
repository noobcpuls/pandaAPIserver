from sqlalchemy.orm import Session
from . import models, schemas

def get_user_by_name(db: Session, name: str):
    return db.query(models.User).filter(models.User.name == name).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, grade=user.grade, is_tested=user.is_tested, timer=user.timer)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_name: str, time: schemas.UserUpdate):
    db_user = db.query(models.User).filter(models.User.name == user_name)
    db_user.update(vars(time))
    db.commit()
    return db_user.first()
