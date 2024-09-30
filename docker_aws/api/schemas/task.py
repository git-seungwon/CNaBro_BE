from pydantic import BaseModel, Field
from datetime import datetime

from typing import List, Optional


# ----- [ user models ] -----

class user(BaseModel):
    user_nickname : Optional[str] 
    email : Optional[str]
    password : Optional[str]
    mobile_number : Optional[str]
    login_at : datetime
    logout_at : datetime
    create_at : datetime
    updated_at : datetime

class user_Create(user):
    pass

class user_Create_Response(user_Create):   
    user_id : int

    class Config:
        orm_mode = True


# ----- [ note models ] -----

class note(BaseModel):
    user_id : int
    content : Optional[str]
    start_time : Optional[datetime]
    end_time : Optional[datetime]
    create_at : Optional[datetime]
    edit_at : datetime
    score : Optional[str]

class note_Create(note):
    pass

class note_Create_Response(note_Create):
    id : int

    class Config:
        orm_mode = True

# ----- [ tag models ] -----

class tag(BaseModel):
    note_id : int
    tag_name : Optional[str]

class tag_Create(tag):
    pass

class tag_Create_Response(tag_Create):
    id : int

    class Config:
        orm_mode = True