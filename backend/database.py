import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = os.getenv('DB_LOCAL_CONN')

def getDb():
    engine = SessionLocal()
    try:
        yield engine
    finally:
        engine.close()

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, # echo=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()