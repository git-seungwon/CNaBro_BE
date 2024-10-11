from passlib.context import CryptContext
from sqlalchemy.orm import Session
from domain.user.user_schemas import UserCreate
from models.tasks import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def create_user(db: Session, user_create: UserCreate):
    db_user = User(username=user_create.user_nickname,
                   password=pwd_context.hash(user_create.password1),
                   email=user_create.email)
    db.add(db_user)
    db.commit()

async def get_existing_user(db: Session, user_create: UserCreate):
    return db.query(User).filter(
        (User.user_nickname == user_create.user_nickname)
        (User.email == user_create.email)
    ).first()