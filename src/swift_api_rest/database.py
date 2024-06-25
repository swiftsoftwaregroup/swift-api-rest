import os

from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool

from sqlalchemy.orm import sessionmaker

load_dotenv()

# default to in-memory SQLite database
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite://")

if SQLALCHEMY_DATABASE_URL == "sqlite://":
    # To use a :memory: database in a multithreaded scenario, 
    # the same connection object must be shared among threads, since the database exists only within the scope of that connection. 
    # The StaticPool implementation will maintain a single connection globally, and the check_same_thread flag can be passed to Pysqlite as False
    engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}, poolclass=StaticPool)
else:    
    engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
