from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, TIMESTAMP, ForeignKey, LargeBinary
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from api.database import Base


class User(Base):
    __tablename__ = 'user'
    
    '''
        필수 데이터

        [email 로그인]
            provider_type
            nickname
            email
            password
            create_at

        [google 로그인]
            provider_id
            provider_type
            nickname
            email
            create_at
    ''' 

    user_id = Column(Integer, primary_key=True, autoincrement=True, comment='유저고유번호')
    provider_id = Column(String(30), nullable=True, comment="OaOauth 제공자가 local이 아닌 경우에만 작성")
    provider_type = Column(String(20), nullable=False, comment="Oauth 제공자 정보")
    nickname = Column(String(20), nullable=False, comment='유저 닉네임')
    email = Column(String(100), nullable=False, comment='유저 이메일')
    password = Column(String(60), nullable=True, comment='유저 비밀번호')
    create_at = Column(DateTime, server_default=func.now(), nullable=False, comment='생성시각')
    update_at = Column(DateTime, nullable=True, comment='최종수정시각')
    profile_url = Column(String(255), nullable=True, comment='프로필 사진 주소')

    notes = relationship("Note", back_populates="user")
    refresh_tokens = relationship("RefreshToken", back_populates="user")
    agreements = relationship("Agreement", back_populates="user")
    login_logs = relationship("LoginLog", back_populates="user")


class Note(Base):
    __tablename__ = 'note'

    '''
        필수 데이터

        user_id, content, start_time, end_time
    '''

    id = Column(Integer, primary_key=True, autoincrement=True, comment='노트 고유번호')
    user_id = Column(Integer, ForeignKey('user.user_id'), nullable=False, comment='유저고유번호')
    content = Column(Text, nullable=False, comment='노트 내용')
    start_time = Column(TIMESTAMP, nullable=False, comment='시작 시간')
    end_time = Column(TIMESTAMP, nullable=False, comment='종료 시간')
    create_at = Column(TIMESTAMP, server_default=func.now(), nullable=False, comment='생성시각')
    update_at = Column(TIMESTAMP, nullable=True, comment='수정 시각')
    score = Column(LargeBinary(2), nullable=False, default=0, comment='집중 단계를 0~3까지 4단계를 2비트로 표현')

    user = relationship("User", back_populates="notes")
    tag_note = relationship("tag_note", back_populates="note")


class tag_note(Base):
    __tablename__ = "tag_note"

    '''
        필수 데이터

        note_id, tag_id
    '''

    id = Column(Integer, primary_key=True, autoincrement=True)
    note_id = Column(Integer, ForeignKey('note.id'), nullable=False, comment='유저고유번호')
    tag_id = Column(Integer, ForeignKey('tag.id'), nullable=False, comment='유저고유번호')
    
    note = relationship("Note", back_populates="tag_note")
    tags = relationship("Tag", back_populates="tag_note")


class Tag(Base):
    __tablename__ = 'tag'

    '''
        필수 데이터

        tag_name
    '''
    
    id = Column(Integer, primary_key=True, autoincrement=True, comment='태그 고유번호')
    tag_name = Column(String(8), nullable=False, comment='태그 이름')

    tag_note = relationship("tag_note", back_populates="tags")


class RefreshToken(Base):
    __tablename__ = 'refresh_token'
    
    '''
        필수 데이터

        user_id, refresh_token, create_at, expire_datetime
    '''

    id = Column(Integer, primary_key=True, autoincrement=True, comment='리프레쉬토큰 고유번호')
    user_id = Column(Integer, ForeignKey('user.user_id'), nullable=False, comment='유저고유번호')
    refresh_token = Column(String(255), nullable=False, comment='리프레쉬토큰')
    create_at = Column(TIMESTAMP, server_default=func.now(), nullable=False, comment='생성시각')
    expire_datetime = Column(TIMESTAMP, nullable=False, comment='만료일시')

    user = relationship("User", back_populates="refresh_tokens")


class Agreement(Base):
    __tablename__ = 'agreement'
    
    '''
        필수 데이터

        user_id
    '''

    id = Column(Integer, primary_key=True, autoincrement=True, comment='동의 고유번호')
    user_id = Column(Integer, ForeignKey('user.user_id'), nullable=False, comment='유저고유번호')
    agree_term = Column(Boolean, nullable=False, default=False, comment='이용약관 동의 여부')
    agree_privacy = Column(Boolean, nullable=False, default=False, comment='개인정보 동의 여부')
    create_at = Column(TIMESTAMP, nullable=False, server_default=func.now(), comment='생성시간')

    user = relationship("User", back_populates="agreements")


class LoginLog(Base):
    __tablename__ = 'login_log'
    
    '''
        필수 데이터

        user_id, login_at
    '''
    
    id = Column(Integer, primary_key=True, autoincrement=True, comment='로그인 기록 고유번호')
    user_id = Column(Integer, ForeignKey('user.user_id'), nullable=False, comment='유저고유번호')
    login_at = Column(TIMESTAMP, nullable=False, server_default=func.now(), comment='로그인 시각')

    user = relationship("User", back_populates="login_logs")
