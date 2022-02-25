from operator import index
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


from .database import Base


class User(Base):
    __tablename__ = "student"

    name = Column(String, primary_key=True, index=True)
    grade = Column(String, index=True)
    is_tested = Column(Boolean, index=True)
    timer = Column(Integer, index=True)