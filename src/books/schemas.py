from pydantic import BaseModel
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

