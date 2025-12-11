from pydantic import BaseModel
from datetime import datetime
import uuid
class Book(BaseModel):
    id:int
    uid:uuid.UUID
    title:str
    author:str
    language:str
    published_date:str
    publisher:str
    created_at:datetime
    updated_at:datetime
    page_count:int


class BookCreateModel(BaseModel):
    id: int
    title: str
    author: str
    language: str
    publisher: str
    published_date: str
    page_count: int

from typing import Optional
class BookUpdateModel(BaseModel):
    
    title: Optional[str] = None
    author: Optional[str] = None
    language: Optional[str] = None
    publisher: Optional[str] = None
    published_date: Optional[str] = None
    page_count: Optional[int] = None

