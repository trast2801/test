from sqlalchemy import create_engine
from sqlalchemy import sessionmaker, DeclorativeBase
from sqlalchemy import Column, Integer, String

engine = create_engine("sqlite:///taskmanager.db", echo = True)
SessionLocal = sessionmaker(bind=engine)

class Base(DeclorativeBase):
    pass
