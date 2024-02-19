from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models import Base, Recipe, Author, Category

engine = create_engine('sqlite:///recipes.db')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
