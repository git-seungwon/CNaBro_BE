from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from urllib.parse import quote

import os
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

user = os.environ["user"]
pwd = os.environ["pwd"]
host = os.environ["host"]
port = os.environ["port"]

db_engine = create_engine(DB_URL, echo=True)
db_session = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)

Base = declarative_base()

def get_db():
    with db_session() as session:
        yield session
