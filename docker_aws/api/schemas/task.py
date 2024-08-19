from pydantic import BaseModel, Field
from datetime import datetime

from typing import List, Optional

class Test(BaseModel):
    id : int
    time : Optional[str] = None
    title : Optional[str] = None
    tag : Optional[str] = None
    emoji : Optional[str] = None

    """ id: int
    contentMain: Optional[str] = Field(None, example='제목')
    time: Optional[datetime] = None
    tag: Optional[str] = None
    score: Optional[int] = None """

class TestBase(BaseModel):
    # contentMain: str | None = Field(None, example="미적분")
    # tag: str | None = Field(None, example="수학")
    # score: str | None = Field(None, example="10")
    time : str | None = Field(None, example="2024-08-01 05:00:10")
    title : str | None = Field(None, example="미적분")
    tag : str | None = Field(None, example="수학")
    emoji : str | None = Field(None, example="1")

class TestCreate(TestBase):
    pass

class TestCreateResponse(TestCreate):
    id : int

    class Config:
        orm_mode = True