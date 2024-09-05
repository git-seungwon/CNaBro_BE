from sqlalchemy import create_engine
from api.models.task import Base

DB_URL = "database://admin:cnabrobe!@database.cd8wseaayh6t.ap-northeast-2.rds.amazonaws.com:3306?charset=utf8"

engine = create_engine(DB_URL, echo=True)

def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    reset_database()
