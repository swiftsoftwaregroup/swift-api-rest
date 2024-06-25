import os
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

# default to in-memory SQLite database
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite://")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
