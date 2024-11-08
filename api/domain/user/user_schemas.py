
from pydantic import BaseModel, EmailStr, field_validator

class LoginRequest(BaseModel):
    email: str
    password: str
    
class UserCreate(BaseModel):
    username: str
    password1: str
    password2: str
    email: EmailStr

    @field_validator('username', 'password1', 'password2', 'email', mode='before')
    def not_empty_string(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v

    @field_validator('username')
    def validate_username_length(cls, v):
        if len(v) > 20:
            raise ValueError('닉네임이 너무 깁니다. 20자 이내로 입력해주세요.')
        return v
        
    @field_validator('password2', mode='before')
    def passwords_match(cls, v, info):
        password1 = info.data.get('password1')
        if password1 and v != password1:
            raise ValueError('비밀번호가 일치하지 않습니다.')
        return v

class Token(BaseModel):
    access_token: str
    token_type: str
    user_id: int

class TokenAuth(BaseModel):
    access_token: str
    token_type: str
    username: str

class User(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        orm_mode = True
