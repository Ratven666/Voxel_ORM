import os.path

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from config import DATABASE_NAME

path = os.path.join("data_bases", DATABASE_NAME)

engine = create_engine(f'sqlite:///{path}')
Session = sessionmaker(bind=engine)

Base = declarative_base()

import db_models


def create_db():
    db_is_created = os.path.exists(path)
    if not db_is_created:
        Base.metadata.create_all(engine)
    else:
        print("Такая БД уже есть!")
