from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from api.db import Base
from datetime import datetime

# class Test(Base):
#     __tablename__ = "test_2_db"

#     """ id = Column(Integer, primary_key=True)
#     contentMain = Column(String(1024))
#     time = Column(DateTime, default=datetime.utcnow)
#     tag = Column(String(20))
#     score = Column(String(2)) """

#     id = Column(Integer, primary_key=True)
#     time = Column(String(20))
#     title = Column(String(128))
#     tag = Column(String(12))
#     emoji = Column(String(2))

class user(Base):
    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True)
    user_nickname = Column(String(10))
    email = Column(String(30))
    password = Column(String(20))
    mobile_number = Column(String(11))
    login_at = Column(datetime)
    logout_at = Column(datetime)
    create_at = Column(datetime)
    update_at = Column(datetime)

class note(Base):
    __tablename__ = "note"

    id = Column(int, primary_key=True)
    user_id = Column(Integer)
    content = Column(String)
    start_time = Column(datetime)
    end_time = Column(datetime)
    creat_at = Column(datetime)
    edit_time = Column(datetime)
    score = Column(int(2))

class tage(Base):
    __tablename__ = "tag"

    id = Column(int, primary_key=True)
    note_id = Column(Integer)
    tag_name = Column(String(8))


