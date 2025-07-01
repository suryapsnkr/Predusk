import redis
import json
from app.schemas import Book

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

def get_books_from_cache():
    data = r.get("books")
    if data:
        return json.loads(data)
    return None

def set_books_in_cache(books):
    r.set("books", json.dumps([book.__dict__ for book in books]), ex=60)
