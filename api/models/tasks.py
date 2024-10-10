from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, TIMESTAMP, ForeignKey, LargeBinary
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from api.database import Base


class User(Base):
    __tablename__ = 'user'
    
    user_id = Column(Integer, primary_key=True, autoincrement=True, comment='유저고유번호')
    user_nickname = Column(String(10), nullable=False, comment='유저 닉네임')
    email = Column(String(30), nullable=False, comment='유저 이메일')
    password = Column(String(20), nullable=True, comment='유저 비밀번호')
    mobile_number = Column(String(11), nullable=False, comment='유저 전화번호')
    create_at = Column(DateTime, server_default=func.now(), nullable=False, comment='생성시각')
    last_update_datetime = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False, comment='최종 변경 시각')
    last_login_datetime = Column(DateTime, nullable=False, comment='최종 로그인 시각')
    last_login_IP = Column(String(50), nullable=False, comment='최종 로그인 IP')
    email_agreement = Column(Boolean, nullable=False, comment='이메일 동의 여부')
    profile_url = Column(String(255), nullable=True, comment='프로필 사진 주소')

    notes = relationship("Note", back_populates="user")
    refresh_tokens = relationship("RefreshToken", back_populates="user")
    agreements = relationship("Agreement", back_populates="user")
    jwt_records = relationship("JWTRecord", back_populates="user")
    login_logs = relationship("LoginLog", back_populates="user")


class Note(Base):
    __tablename__ = 'note'
    
    id = Column(Integer, primary_key=True, autoincrement=True, comment='노트 고유번호')
    user_id = Column(Integer, ForeignKey('user.user_id'), nullable=False, comment='유저고유번호')
    content = Column(Text, nullable=False, comment='노트 내용')
    start_time = Column(TIMESTAMP, nullable=False, comment='시작 시간')
    end_time = Column(TIMESTAMP, nullable=False, comment='종료 시간')
    create_at = Column(TIMESTAMP, server_default=func.now(), nullable=False, comment='생성시각')
    edit_at = Column(TIMESTAMP, nullable=True, comment='수정 시각')
    score = Column(LargeBinary(2), nullable=False, default=0, comment='점수')

    user = relationship("User", back_populates="notes")
    tags = relationship("Tag", back_populates="note")


class Tag(Base):
    __tablename__ = 'tag'
    
    id = Column(Integer, primary_key=True, autoincrement=True, comment='태그 고유번호')
    note_id = Column(Integer, ForeignKey('note.id'), nullable=False, comment='노트 고유번호')
    tag_name = Column(String(8), nullable=False, comment='태그 이름')

    note = relationship("Note", back_populates="tags")


class RefreshToken(Base):
    __tablename__ = 'refresh_token'
    
    id = Column(Integer, primary_key=True, autoincrement=True, comment='리프레쉬토큰 고유번호')
    user_id = Column(Integer, ForeignKey('user.user_id'), nullable=False, comment='유저고유번호')
    refresh_token = Column(String(255), nullable=False, comment='리프레쉬토큰')
    create_at = Column(TIMESTAMP, server_default=func.now(), nullable=False, comment='생성시각')
    expire_datetime = Column(TIMESTAMP, nullable=False, comment='만료일시')
    token_type = Column(Integer, nullable=True, comment='토큰 유형 (0: Email, 1: Google, 2: Apple)')

    user = relationship("User", back_populates="refresh_tokens")


class Agreement(Base):
    __tablename__ = 'agreement'
    
    id = Column(Integer, primary_key=True, autoincrement=True, comment='동의 고유번호')
    user_id = Column(Integer, ForeignKey('user.user_id'), nullable=False, comment='유저고유번호')
    agree_term = Column(Integer, nullable=True, default=0, comment='이용약관 동의 여부')
    agree_privacy = Column(Integer, nullable=True, default=0, comment='개인정보 동의 여부')
    agree_sensitive = Column(Integer, nullable=True, default=0, comment='민감정보 동의 여부')
    create_at = Column(TIMESTAMP, server_default=func.now(), nullable=False, comment='생성시각')

    user = relationship("User", back_populates="agreements")


class JWTRecord(Base):
    __tablename__ = 'jwt_record'
    
    id = Column(Integer, primary_key=True, autoincrement=True, comment='발급 고유번호')
    refresh_token_id = Column(Integer, ForeignKey('refresh_token.id'), nullable=False, comment='리프레쉬토큰 고유번호')
    user_id = Column(Integer, ForeignKey('user.user_id'), nullable=False, comment='유저고유번호')
    ip_address = Column(String(20), nullable=True, comment='아이피 주소')
    expire_datetime = Column(DateTime, nullable=False, comment='만료일시')
    logout_at = Column(TIMESTAMP, nullable=True, comment='로그아웃 시각')
    create_at = Column(TIMESTAMP, server_default=func.now(), nullable=False, comment='생성시각')

    user = relationship("User", back_populates="jwt_records")
    refresh_token = relationship("RefreshToken")


class LoginLog(Base):
    __tablename__ = 'login_log'
    
    id = Column(Integer, primary_key=True, autoincrement=True, comment='로그인 기록 고유번호')
    user_id = Column(Integer, ForeignKey('user.user_id'), nullable=False, comment='유저고유번호')
    login_at = Column(DateTime, nullable=True, comment='로그인 시각')
    login_IP = Column(String(50), nullable=True, comment='로그인 IP')

    user = relationship("User", back_populates="login_logs")
