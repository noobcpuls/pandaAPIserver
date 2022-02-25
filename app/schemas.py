from typing import Optional
from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    grade: str
    is_tested: bool
    timer: int

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    timer: int

class User(UserBase):
    name: str
    grade: str
    is_tested: bool
    timer: int

    class Config:
        orm_mode = True