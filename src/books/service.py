from typing import List
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime
from .schemas import Book as BookSchema, BookCreateModel, BookUpdateModel
from src.db.models import Book as BookModel  # SQLModel DB model

class BookService:

    async def get_all_books(self, session: AsyncSession) -> List[BookSchema]:
        result = await session.execute(select(BookModel).order_by(BookModel.created_at.desc()))
        books = result.scalars().all()  # List of SQLModel objects
        # Convert each SQLModel object to Pydantic
        return [BookSchema.from_orm(book) for book in books]
        
    async def get_user_books(self,user_uid:str, session: AsyncSession) -> List[BookSchema]:
        result = await session.execute(select(BookModel).where(BookModel.user_uid == user_uid).order_by(BookModel.created_at.desc()))
        books = result.scalars().all()  # List of SQLModel objects
        # Convert each SQLModel object to Pydantic
        return [BookSchema.from_orm(book) for book in books]
        
    async def get_book(self, book_uid, session: AsyncSession):
        return await session.get(BookModel, book_uid)
       

    async def create_book(self, book_data: BookCreateModel,user_uid:str, session: AsyncSession):
        book_data_dict = book_data.model_dump()
        new_book = BookModel(**book_data_dict)
        
        new_book.user_uid = user_uid
        session.add(new_book)
        await session.commit()
        await session.refresh(new_book)
        return BookSchema.from_orm(new_book)

    async def update_book(self, book_uid, book_update_data: BookUpdateModel, session: AsyncSession):
        book = await session.get(BookModel, book_uid)
        if not book:
            return None
        for key, value in book_update_data.dict(exclude_unset=True).items():
            setattr(book, key, value)
        await session.commit()
        await session.refresh(book)
        return BookSchema.from_orm(book)

    async def delete_book(self, book_uid, session: AsyncSession):
        book = await session.get(BookModel, book_uid)
        if not book:
            return False
        await session.delete(book)
        await session.commit()
        return True
