from sqlmodel import SQLModel, Field, Column
from datetime import datetime, date
import uuid
import sqlalchemy.dialects.postgresql as pg

class Book(SQLModel, table=True):
    __tablename__ = "books"

    uid: uuid.UUID = Field(
        sa_column=Column(pg.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    )
    title: str
    author: str
    language: str
    published_date: date
    publisher: str
    page_count: int
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
