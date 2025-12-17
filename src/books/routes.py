from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
import uuid
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import Book, BookCreateModel, BookUpdateModel,BookDetailModel
from src.books.service import BookService
from src.db.main import get_session
from src.auth.dependencies import AccessTokenBearer,RoleChecker
from src.errors import BookNotFound


book_router = APIRouter()
book_service = BookService()
access_token_bearer = AccessTokenBearer()
role_checker = Depends(RoleChecker(['admin','user']))


@book_router.get("/", response_model=List[Book],dependencies=[role_checker])
async def get_all_books(
    session: AsyncSession = Depends(get_session),
    token_details:dict=Depends(access_token_bearer),
)->dict:
    print(token_details)
    return await book_service.get_all_books(session)


@book_router.get("/user/{user_uid}", response_model=List[Book],dependencies=[role_checker])
async def get_user_book_submissions(
    user_uid: uuid.UUID,
    session: AsyncSession = Depends(get_session),
    token_details:dict=Depends(access_token_bearer),
)->dict:
    user_uid = token_details["user"]["user_uid"]
    books = await book_service.get_user_books(user_uid,session)
    return books
    

@book_router.post("/", status_code=status.HTTP_201_CREATED, response_model=Book,dependencies=[role_checker])
async def create_a_book(
    book_data: BookCreateModel, session: AsyncSession = Depends(get_session),
    token_details:dict=Depends(access_token_bearer),
) ->dict:
    user_id = token_details['user']['user_uid']
    new_book = await book_service.create_book(book_data,user_id,session)
    return new_book
    

@book_router.get("/{book_uid}", response_model=BookDetailModel,dependencies=[role_checker])
async def get_a_book(
    book_uid: uuid.UUID, session: AsyncSession = Depends(get_session),
    token_details:dict=Depends(access_token_bearer),
) ->dict:
    book = await book_service.get_book(book_uid, session)
    if not book:
        raise BookNotFound()
    return book

@book_router.patch("/{book_uid}", response_model=Book,dependencies=[role_checker])
async def update_book(
    book_uid: uuid.UUID, book_update_data: BookUpdateModel, session: AsyncSession = Depends(get_session),
    token_details:dict=Depends(access_token_bearer),
) ->dict:
    updated_book = await book_service.update_book(book_uid, book_update_data, session)
    if not updated_book:
        raise BookNotFound()
    return updated_book

@book_router.delete("/{book_uid}", status_code=status.HTTP_204_NO_CONTENT,dependencies=[role_checker])
async def delete_a_book(
    book_uid: uuid.UUID, session: AsyncSession = Depends(get_session),
    token_details:dict=Depends(access_token_bearer),
):
    deleted = await book_service.delete_book(book_uid, session)
    if not deleted:
        raise BookNotFound()
    else:
        return {}


