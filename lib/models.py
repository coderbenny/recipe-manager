from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base() 

# Recipe class
class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    ingredients = Column(String())
    instructions = Column(String())

    category_id = Column(Integer(), ForeignKey('categories.id'))
    author_id = Column(Integer(), ForeignKey('authors.id'))

    def __repr__(self):
        return f'Recipe {self.name}, ' + \
            f'{self.ingredients}'
    
    # Retrieve all recipes
    @classmethod
    def all_recipes(cls, session):
        return session.query(Recipe).all()

    # Create new recipe
    @classmethod
    def create_recipe(cls, session, name, ingredients, instructions, category_id, author_id):
        new_recipe = Recipe(name=name, ingredients=ingredients, instructions=instructions, category_id=category_id, author_id=author_id)
        session.add(new_recipe)
        session.commit()
        return new_recipe

    # Remove a recipe
    @classmethod
    def remove_recipe(cls, session, recipe_id):
        recipe = session.query(Recipe).get(recipe_id)
        if recipe:
            session.delete(recipe)
            session.commit()
            return "Recipe deleted succesfully"
        else:
            return "Recipe does not exist!"

    # Search for a recipe
    @classmethod
    def search(cls, session, keyword):
        return session.query(Recipe).filter(Recipe.name.ilike(f'%{keyword}%')).all()

# Category class
class Category(Base):
    __tablename__ = 'categories'    

    id = Column(Integer(), primary_key=True)
    title = Column(String())

    recipes = relationship('Recipe', backref=backref('category')) 

    def __repr__(self):
        return f'Category {self.title}'
    
    # Retrieve all categories
    @classmethod
    def all_categories(cls, session):
        return session.query(Category).all()

    # Add a new category
    @classmethod
    def add_category(cls, session, title):
        new_category = Category(title=title)
        session.add(new_category)
        session.commit()
        return new_category

# Author class
class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    recipes = relationship('Recipe', backref=backref('author')) 


    def __repr__(self):
        return f'Author {self.name}'

    # Retrieve all authors
    @classmethod
    def all_authors(cls, session):
        return session.query(Author).all()

    # Add an author
    @classmethod
    def add_author(cls, session, name):
        new_author = Author(name=name)
        session.add(new_author)
        session.commit()
        return new_author
