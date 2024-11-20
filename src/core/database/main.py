from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///src/storage/database.db")

Session = sessionmaker(bind=engine)
session = Session()

base = declarative_base()
