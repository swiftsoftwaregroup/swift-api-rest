from datetime import date
from pydantic import BaseModel

class BookSchema(BaseModel):
    title: str
    author: str
    date_published: date
    cover_image: str

class BookCreate(BookSchema):
    pass

class Book(BookSchema):
    id: int

    class Config:
        from_attributes = True