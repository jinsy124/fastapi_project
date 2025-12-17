from src.db.models import User
from sqlmodel.ext.asyncio.session import AsyncSession
from .utilis import generate_passwd_hash
from sqlmodel import select
from .schemas import UserCreateModel

class UserService:
    async def get_user_email(self, email: str, session: AsyncSession):
        statement = select(User).where(User.email == email)
        result = await session.execute(statement)
        user = result.scalar_one_or_none() 
        return  user

    async def user_exists(self, email: str, session: AsyncSession) -> bool:
        user = await self.get_user_email(email, session)
        return True if user is not None else False

    async def create_user(self, user_data: UserCreateModel, session: AsyncSession):
        user_data_dict = user_data.model_dump()

        new_user = User(
            **user_data_dict
        )
        new_user.password_hash = generate_passwd_hash(user_data_dict['password'])
        new_user.role = "user"

        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)
        return new_user
