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

class jwt_record(Base):
    __tablename__ = "jwt_record"

    id = Column(Integer, primary_key=True)
    refresh_token_id = Column(Integer, ForeignKey)
    user_id = Column(Integer, ForeignKey("user.user_id"))
    ip_address = Column(String(20))
    expire_datetime = Column(DateTime)
    logout_at = Column(DateTime)
    create_at = Column(DateTime)

class refresh_token(Base):
    __tablename__ = "refresh_token"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.user_id"))
    refresh_token = Column(type)
    create_at = Column(DateTime)
    expire_datetime = Column(DateTime)
    token_type = (Integer)

class agreement(Base):
    __tablename__ = "agreement"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.user_id"))
    agree_term = Column(Integer)
    agree_privacy = Column(Integer)
    agree_sensitive = Column(Integer)
    create_at = Column(DateTime)

class login_log(Base):
    __tablename__ = "login_log"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.user_id"))
    login_at = Column(DateTime)
    login_ip = Column(String(50))






