
from passlib.context import CryptContext
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from api.domain.user.user_schema import UserCreate
from api.models.ORM import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def create_user(db: AsyncSession, user_create: UserCreate):
    db_user = User(user_nickname=user_create.username,
                   password=pwd_context.hash(user_create.password1),
                   email=user_create.email)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)

async def get_existing_user(db: AsyncSession, user_create: UserCreate):
    result: Result = await db.execute(
        select(User).filter(
            (User.user_nickname == user_create.username) |
            (User.email == user_create.email)
        )
    )
    return result.scalars().all()

async def get_user(db: AsyncSession, username: str) -> User:
    result : Result = await db.execute(select(User).filter(User.user_nickname == username))
    return result.scalar_one_or_none()

async def get_user_by_userid(db: AsyncSession, user_id: int) -> User:
    result : Result = await db.execute(select(User).filter(User.user_id == user_id))
    return result.scalar_one_or_none()

async def get_user_by_email(db: AsyncSession, email: str) -> User:
    result : Result = await db.execute(select(User).filter(User.email == email))
    return result.scalar_one_or_none()


