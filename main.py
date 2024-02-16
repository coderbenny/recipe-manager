from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models import Base

if __name__ == '__main__':
    engine = create_engine('sqlite:///recipes.db')
    Base.metadata.create_all(engine)
    
    Session = sessionmaker(bind=engine)
    session = Session()