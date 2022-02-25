from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgres://uonsteyxfduahf:75f7611acecc70b4298612f838c729904f8da55e5ffea539f164495803282e60@ec2-18-210-159-154.compute-1.amazonaws.com:5432/d6mosa6s8u3112"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()