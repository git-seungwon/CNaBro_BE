from pydantic import BaseModel, Field
from datetime import datetime

from typing import List, Optional

class user(BaseModel):
    user_nickname : Optional[str] 
    email : Optional[str]
    password : Optional[str]
    mobile_number : Optional[str]
    login_at : datetime
    logout_at : datetime
    create_at : datetime
    updated_at : datetime

class userCreate(user):
    pass

class userCreateResponse(userCreate):   
    user_id : int

    class Config:
        orm_mode = True

class note(BaseModel):
    user_id : int
    content : Optional[str]
    start_time : Optional[datetime]
    end_time : Optional[datetime]
    create_at : Optional[datetime]
    edit_at : datetime
    score : Optional[str]

class noteCreate(note):
    pass

class noteCreateResponse(noteCreate):
    id : int

    class Config:
        orm_mode = True



class tag(BaseModel) :
    note_id : int
    tag_name : Optional[str]