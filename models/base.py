from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from data.config import DATABASE_ENGINE

# создать движок и начать взаимодействовать с базами данных
engine = create_engine(DATABASE_ENGINE)
Session = sessionmaker(bind=engine)

Base = declarative_base()
