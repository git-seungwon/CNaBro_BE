

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

# ----- [ jwt_record models ] -----

class jwt_record(BaseModel):
    refresh_token_id : int
    user_id : int 
    id_address : Optional[str]
    expire_datetime : datetime
    logout_at : Optional[datetime]
    creat_at : datetime

class jwt_record_create(jwt_record):
    pass 

class jwt_record_create_Response(jwt_record_create):
    id : int

    class Config:
        orm_mode = True

# ----- [ refresh_token models ] -----

class refresh_tocken(BaseModel):
    user_id : int
    refresh_tocken : type
    create_at : datetime
    expire_datetime : datetime

class refresh_token_create(refresh_tocken):
    pass 

class refresh_tocken_create_Response(refresh_token_create):
    id : int

    class Config:
        orm_mode = True

# ------ [ agreement models ] -----

class agreement(BaseModel):
    user_id : int
    agree_term : Optional[int]
    agree_privacy : Optional[int]
    agree_sensitive : Optional[int]
    create_at : datetime

class agreement_create(agreement):
    pass 

class agreement_create_Response(agreement_create):
    id : int

    class config:
        orm_mode = True

# ----- [ login_log models ] -----

class login_log(BaseModel):
    user_id : int
    login_at : Optional[datetime]

class login_log_create(login_log):
    pass 

class login_log_create_Response(login_log_create):
    id : int

    class config:
        orm_mode = True

