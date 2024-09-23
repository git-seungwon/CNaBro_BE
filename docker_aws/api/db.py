from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# DB_URL = "mysql+pymysql://root@db:3306/demo?charset=utf8"
# DB_URL = "mysql+pymysql://admin:cnabrobe!@database.cd8wseaayh6t.ap-northeast-2.rds.amazonaws.com:3306/demo?charset=utf8"
DB_URL = "mysql+pymysql://admin:cnabrobe!@database.cd8wseaayh6t.ap-northeast-2.rds.amazonaws.com:3306?charset=utf8"

#arn:aws:rds:ap-northeast-2:730335663316:db:database

#mysql -u admin -p -h database.cd8wseaayh6t.ap-northeast-2.rds.amazonaws.com
#dialect+driver://username:password@host:port/database


db_engine = create_engine(DB_URL, echo=True)
db_session = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)

Base = declarative_base()

def get_db():
    with db_session() as session:
        yield session
