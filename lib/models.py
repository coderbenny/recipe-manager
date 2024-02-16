from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base() 

# Recipe class
class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    ingredients = Column(String())
    instructions = Column(String())

    def __repr__(self):
        return f'Recipe {self.name}, ' + \
            f'{self.ingredients}'

# Category class
class Category(Base):
    __tablename__ = 'categories'    

    id = Column(Integer(), primary_key=True)
    title = Column(String())

    def __repr__(self):
        return f'Category {self.title}'

# Author class
class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    def __repr__(self):
        return f'Author {self.name}'

