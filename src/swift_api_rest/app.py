from typing import List

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIRoute

from sqlalchemy.orm import Session

from .database import get_db, engine
from .models_db import Base, BookModel
from .models_api import Book, BookCreate

# Create the database tables
Base.metadata.create_all(bind=engine)

# Create the FastAPI app
app = FastAPI(
    title="Book Management API",
    description="A simple API for managing books",
    version="1.0.0"
)

# CORS
origins = [
    # local testing with Angular
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Web API
@app.get("/", tags=["Root"])
async def get_root():
    """
    The root endpoint can serve as healthcheck
    """    
    return {"message": "Swift API REST"}

@app.get("/ping", tags=["Root"])
async def ping():
    """
    Simple endpoint to test API liveness
    """    
    return "PONG"


# Tags for API documentation
tags_metadata = [
    {
        "name": "books",
        "description": "Operations with books. Manage the book inventory."
    }
]

@app.post("/books/", response_model=Book, tags=["books"])
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    """
    Create a new book with the given details.
    """    
    db_book = BookModel(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@app.get("/books/", response_model=List[Book], tags=["books"])
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve a list of books. You can specify how many to skip and the limit of books to return.
    """    
    books = db.query(BookModel).offset(skip).limit(limit).all()
    return books

@app.get("/books/{book_id}", response_model=Book, tags=["books"])
def read_book(book_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a specific book by its ID.
    """    
    book = db.query(BookModel).filter(BookModel.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.put("/books/{book_id}", response_model=Book, tags=["books"])
def update_book(book_id: int, book: BookCreate, db: Session = Depends(get_db)):
    """
    Update a book's information given its ID.
    """    
    db_book = db.query(BookModel).filter(BookModel.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    for key, value in book.dict().items():
        setattr(db_book, key, value)
    db.commit()
    db.refresh(db_book)
    return db_book

@app.delete("/books/{book_id}", response_model=Book, tags=["books"])
def delete_book(book_id: int, db: Session = Depends(get_db)):
    """
    Delete a book given its ID.
    """    
    book = db.query(BookModel).filter(BookModel.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return book


def use_route_names_as_operation_ids() -> None:
    """
    Simplify operation IDs so that generated API clients have simpler function
    names.

    Should be called only after all routes have been added.
    """
    for route in app.routes:
        if isinstance(route, APIRoute):
            route.operation_id = route.name  # in this case, 'ping' and 'root'


use_route_names_as_operation_ids()
