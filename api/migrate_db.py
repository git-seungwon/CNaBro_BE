from sqlalchemy import create_engine
from api.models.task import Base
from urllib.parse import quote

import os
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

user = os.environ["user"]
pwd = os.environ["pwd"]
host = os.environ["host"]
port = os.environ["port"]

DB_URL = f'mysql+pymysql://{user}:{quote(pwd)}@{host}:{port}/demo?charset=utf8mb4'

engine = create_engine(DB_URL, echo=True)

def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    reset_database()