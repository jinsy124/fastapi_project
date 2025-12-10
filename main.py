from fastapi import FastAPI,status
from pydantic import BaseModel
from fastapi.exceptions import HTTPException
app = FastAPI()

books = [
    {
        "id": 1,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "language": "English",
        "published_year": 1925,
        "publisher": "Charles Scribner's Sons",
    },
    {
        "id": 2,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "language": "English",
        "published_year": 1960,
        "publisher": "J.B. Lippincott & Co.",
    },
    {
        "id": 3,
        "title": "1984",
        "author": "George Orwell",
        "language": "English",
        "published_year": 1949,
        "publisher": "Secker & Warburg",
    },
]


class Book(BaseModel):
    id:int
    title:str
    author:str
    language:str
    published_year:int
    publisher:str

class BookUpdateModel(BaseModel):
    
    title:str
    author:str
    language:str
    
    publisher:str






@app.get("/books")
async def get_all_books():
    return books

@app.post("/books",status_code=status.HTTP_201_CREATED)
async def crate_a_book(book_data:Book)->dict:
    new_book=book_data.model_dump()
    books.append(new_book)
    return new_book
    

@app.get("/books/{book_id}")
async def get_a_book(book_id: int)->dict:
    for book in books:
        if book["id"]==book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book not found")
@app.patch("/book/{book_id}")
async def update_book(boook_id:int,book_update_data:BookUpdateModel)->dict:
    for book in books:
        if book["id"]==boook_id:
            book["title"]=book_update_data.title
            book["author"]=book_update_data.author
            book["language"]=book_update_data.language
            book["publisher"]=book_update_data.publisher
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book not found")


@app.delete("/books/{book_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_a_book(book_id:int):
    for book in books:
        if book["id"]==book_id:
            books.remove(book)
            return {}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book not found")