from typing import List
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import Book as BookSchema, BookCreateModel, BookUpdateModel
from .models import Book as BookModel  # SQLModel DB model

class BookService:

    async def get_all_books(self, session: AsyncSession) -> List[BookSchema]:
        result = await session.execute(select(BookModel).order_by(BookModel.created_at.desc()))
        books = result.scalars().all()  # List of SQLModel objects
        # Convert each SQLModel object to Pydantic
        return [BookSchema.from_orm(book) for book in books]
        

    async def get_book(self, book_uid, session: AsyncSession):
        result = await session.get(BookModel, book_uid)
        if result:
            return BookSchema.from_orm(result)
        return None

    async def create_book(self, book_data: BookCreateModel, session: AsyncSession):
        book = BookModel(**book_data.dict())
        session.add(book)
        await session.commit()
        await session.refresh(book)
        return BookSchema.from_orm(book)

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
