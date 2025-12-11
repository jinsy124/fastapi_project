from src.books.schemas import Book
import uuid
from datetime import datetime



books = [
    {
        "id": 1,
        "uid": str(uuid.uuid4()),
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "language": "English",
        "published_date": "1925",
        "publisher": "Charles Scribner's Sons",
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
        "page_count": 218
    },
    {
        "id": 2,
        "uid": str(uuid.uuid4()),
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "language": "English",
        "published_date": "1960",
        "publisher": "J.B. Lippincott & Co.",
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
        "page_count": 281
    },
    {
        "id": 3,
        "uid": str(uuid.uuid4()),
        "title": "1984",
        "author": "George Orwell",
        "language": "English",
        "published_date": "1949",
        "publisher": "Secker & Warburg",
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
        "page_count": 328
    },
]
