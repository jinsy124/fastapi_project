from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from src.config import Config

# 1. Create async engine correctly
engine = create_async_engine(
    Config.DATABASE_URL,
    echo=True
)

# 2. Create sessionmaker correctly
async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# 3. Initialize DB
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

# 4. Dependency for routes
async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
