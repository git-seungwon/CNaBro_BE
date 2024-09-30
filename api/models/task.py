from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from api.db import Base

class User(Base):
    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True, index=True)
    user_nickname = Column(String(10), nullable=True)
    email = Column(String(30), nullable=True)
    password = Column(String(20), nullable=True)
    mobile_number = Column(String(11), nullable=True)
    login_at = Column(DateTime)
    logout_at = Column(DateTime)
    create_at = Column(DateTime) 
    updated_at = Column(DateTime) 

class Note(Base):
    __tablename__ = "note"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.user_id"))
    content = Column(Text)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    creat_at = Column(DateTime)
    edit_time = Column(DateTime)
    score = Column(Integer)
    
    user = relationship("User", backref="addresses", order_by=id)

class Tage(Base):
    __tablename__ = "tag"

    id = Column(Integer, primary_key=True)
    note_id = Column(Integer)
    tag_name = Column(String(8))

