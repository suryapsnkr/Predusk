from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app import models, schemas, crud, database, cache

app = FastAPI()

@app.on_event("startup")
def startup():
    database.init_db()

@app.get("/books", response_model=list[schemas.Book])
def get_books(db: Session = Depends(database.get_db)):
    try:
        cached = cache.get_books_from_cache()
        if cached:
            return cached
    except Exception:
        print("Redis unavailable, falling back to DB")

    books = crud.get_books(db)
    try:
        cache.set_books_in_cache(books)
    except Exception:
        print("Redis unavailable for setting cache")
    return books

@app.post("/books", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(database.get_db)):
    return crud.create_book(db, book)

@app.get("/books/{book_id}/reviews", response_model=list[schemas.Review])
def get_reviews(book_id: int, db: Session = Depends(database.get_db)):
    return crud.get_reviews_by_book(db, book_id)

@app.post("/books/{book_id}/reviews", response_model=schemas.Review)
def create_review(book_id: int, review: schemas.ReviewCreate, db: Session = Depends(database.get_db)):
    return crud.create_review(db, book_id, review)
