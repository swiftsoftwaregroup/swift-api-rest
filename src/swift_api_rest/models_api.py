from typing import Optional

from datetime import date
from pydantic import BaseModel, Field

class BookSchema(BaseModel):
    title: str = Field(..., description="The title of the book", example="To Kill a Mockingbird")
    author: str = Field(..., description="The author of the book", example="Harper Lee")
    date_published: date = Field(..., description="The publication date of the book", example="1960-07-11")
    cover_image: str = Field(..., description="URL to the book's cover image", example="http://example.com/cover.jpg")

class BookCreate(BookSchema):
    pass

class Book(BookSchema):
    id: int = Field(..., description="The unique identifier of the book", example=1)

    class Config:
        from_attributes = True
