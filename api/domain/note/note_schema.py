from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional
import datetime

class NoteRequest(BaseModel):
    pass

class Notes(BaseModel): 
    ''' 노트 반환 시 제공될 정보 '''

    user_id: int
    content: str
    start_time: datetime.datetime
    end_time: datetime.datetime
    create_at: datetime.datetime
    edit_at: datetime.datetime
    score: int

    class Config:
        orm_mode = True

class NoteCreate(BaseModel):
    ''' 노트 생성 시 필수로 작성해야 하는 항목, user_id는 JWT 토큰 내부에 들어 있기 때문에 제외. '''
    content: str
    start_time: datetime.datetime
    end_time: datetime.datetime
    
    @field_validator('content', mode='before')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v
    
class NoteUpdate(BaseModel):
    content: Optional[str] = None
    note_id: int

class NoteList(BaseModel):
    total: int = 0
    note_list: list[Notes] = []

class NoteDelete(BaseModel):
    note_id: int