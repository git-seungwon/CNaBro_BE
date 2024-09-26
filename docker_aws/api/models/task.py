from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, TIMESTAMP, Text, Date
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
    login_at = Column(TIMESTAMP)
    logout_at = Column(TIMESTAMP)
    create_at = Column(TIMESTAMP) 
    updated_at = Column(TIMESTAMP) 

class Note(Base):
    __tablename__ = "note"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.user_id"))
    content = Column(Text)
    start_time = Column(TIMESTAMP)
    end_time = Column(TIMESTAMP)
    creat_at = Column(TIMESTAMP)
    edit_time = Column(TIMESTAMP)
    score = Column(Integer)
    
    user = relationship("User", backref="addresses", order_by=id)

class Tage(Base):
    __tablename__ = "tag"

    id = Column(Integer, primary_key=True)
    note_id = Column(Integer)
    tag_name = Column(String(8))


