from pydantic import BaseModel
from datetime import datetime, date
from src.reviews.schemas import ReviewModel
import uuid
from typing import Optional,List



class Book(BaseModel):
    uid: uuid.UUID
    title: str
    author: str
    language: str
    published_date: date
    publisher: str
    page_count: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
    model_config = {
        "from_attributes": True
    }


class BookDetailModel(Book):
    reviews:List[ReviewModel] = []
        


    
class BookCreateModel(BaseModel):
    title: str
    author: str
    language: str
    publisher: str
    published_date: date
    page_count: int

class BookUpdateModel(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    language: Optional[str] = None
    publisher: Optional[str] = None
    published_date: Optional[date] = None
    page_count: Optional[int] = None
    


    
