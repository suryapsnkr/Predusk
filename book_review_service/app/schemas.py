from pydantic import BaseModel
from datetime import datetime

class BookCreate(BaseModel):
    title: str
    author: str
    published_date: str

class Book(BookCreate):
    id: int
    class Config:
        orm_mode = True

class ReviewCreate(BaseModel):
    rating: int
    review_text: str

class Review(ReviewCreate):
    id: int
    created_at: datetime
    class Config:
        orm_mode = True
