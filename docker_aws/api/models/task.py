from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from api.db import Base
from datetime import datetime

class Test(Base):
    __tablename__ = "test_2_db"

    """ id = Column(Integer, primary_key=True)
    contentMain = Column(String(1024))
    time = Column(DateTime, default=datetime.utcnow)
    tag = Column(String(20))
    score = Column(String(2)) """
    
    id = Column(Integer, primary_key=True)
    time = Column(String(20))
    title = Column(String(128))
    tag = Column(String(12))
    emoji = Column(String(2))