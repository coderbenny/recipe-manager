from sqlalchemy import create_engine
from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base() 

engine = create_engine('sqlite:///recipes.db')
Session = sessionmaker(bind=engine)


if __name__ == '__main__':
    Base.metadata.create_all(engine)