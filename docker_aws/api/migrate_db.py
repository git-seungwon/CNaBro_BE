from sqlalchemy import create_engine
from api.models.task import Base
from urllib.parse import quote

user = "admin"
pwd = "cnabrobe!"
host = "database.cd8wseaayh6t.ap-northeast-2.rds.amazonaws.com"
port = 3306
DB_URL = f'mysql+pymysql://{user}:{quote(pwd)}@{host}:{port}/demo?charset=utf8mb4'

engine = create_engine(DB_URL, echo=True)

def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    reset_database()