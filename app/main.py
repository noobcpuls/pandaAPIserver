from cmath import exp
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session
import os
from . import crud, models, schemas
from .database import SessionLocal, engine
from . import mydata

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Item(BaseModel):
    name: str
    grade: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/users/{user_name}", response_model=schemas.User)
def read_user(user_name: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_name(db, name=user_name)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.get("/testfile/")
def read_file(user_name: str, number: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_name(db, name=user_name)
    grade = db_user.grade
    grades = mydata.grades
    words = grade.split("/")
    print(words)
    try :
        word = words[number]
        abs_path = os.path.abspath(grades[word])
        print(abs_path)
        if (os.path.exists(abs_path)):
            return FileResponse(abs_path)
        raise HTTPException(status_code=404, detail="File not found")
    except KeyError:
        raise HTTPException(status_code=404, detail="Grade not found")
    except IndexError:
        raise HTTPException(status_code=404, detail="Out of ranged index")
    except AttributeError:
        raise HTTPException(status_code=404, detail="User Not Found")


@app.post("/test/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_name(db, name=user.name)
    if db_user:
        raise HTTPException(status_code=400, detail="Name already existed")
    return crud.create_user(db=db, user=user)

@app.put("/test/update/", response_model=schemas.User)
def update_user(user_name: str, time: schemas.UserUpdate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_name(db, name=user_name)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        return crud.update_user(db=db, user_name=user_name, time=time)


