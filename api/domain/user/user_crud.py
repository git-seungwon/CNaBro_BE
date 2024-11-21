
from passlib.context import CryptContext
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from api.domain.user.user_schema import UserCreate, SocialMember
from api.models.ORM import User
from api.domain.user import user_schema
from api.models.ORM import LoginLog

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def delete_user(db: AsyncSession, current_user:User):
    await db.delete(current_user)
    await db.commit()

async def create_user(db: AsyncSession, user_create: UserCreate):
    db_user = User(nickname=user_create.nickname,
                   password=pwd_context.hash(user_create.password1),
                   email=user_create.email,
                   provider_type="email")
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)

async def create_social_user(db: AsyncSession, user_create: SocialMember):
    db_user = User(nickname=user_create.nickname,
                   email=user_create.email,
                   provider_type=user_create.provider.name,
                   provider_id=int(user_create.provider_id))
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)

async def get_existing_user(db: AsyncSession, user_create: UserCreate):
    result: Result = await db.execute(
        select(User).filter(
            (User.nickname == user_create.nickname) |
            (User.email == user_create.email)
        )
    )
    return result.scalars().all()

async def get_user(db: AsyncSession, nickname: str) -> User:
    result : Result = await db.execute(select(User).filter(User.nickname == nickname))
    return result.scalar_one_or_none()

async def get_user_by_userid(db: AsyncSession, user_id: int) -> User:
    result : Result = await db.execute(select(User).filter(User.user_id == user_id))
    return result.scalar_one_or_none()

async def get_user_by_email(db: AsyncSession, email: str) -> User:
    result : Result = await db.execute(select(User).filter(User.email == email))
    return result.scalar_one_or_none()

async def get_user_by_sub(db: AsyncSession, sub: str) -> User:
    result : Result = await db.execute(select(User).filter(User.provider_id == sub))
    return result.scalar_one_or_none()

async def get_user_update(db:AsyncSession, db_user:User, user_update: user_schema.userupdate):
    if user_update.nickname is not None:   
        db_user.nickname = user_update.nickname
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)

async def create_loginlog(db: AsyncSession,  user: User):
    db_log = LoginLog(user_id=user.user_id)
    db.add(db_log)
    await db.commit()
    await db.refresh(db_log)