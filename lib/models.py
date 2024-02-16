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
        return f'Recipe: {self.name}, ' + \
            f'Ingredients: {self.ingredients}'
    
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
            print("Recipe deleted succesfully")
            return recipe
        else:
            print("Recipe does not exist!")
            return None

    # Search for a recipe based on the ingredient specified
    @classmethod
    def search_by_ingredient(cls, session, ingredient):
        return session.query(Recipe).filter(Recipe.ingredients.ilike(f'%{ingredient}%')).all()

    # search for a recipe by the author name
    @classmethod
    def search_by_author(cls, session, author_name):
        author = session.query(Author).filter_by(name=author_name).first()
        if author:
            recipes = session.query(Recipe).filter_by(author_id=author.id).all()
            if recipes:
                return recipes
            else:
                print("The author does not have any recipes")
                return []
        else:
            print("Author does not exist!")
            return []


    # search for a recipe by the category name
    @classmethod
    def search_by_category(cls, session, category_name):
        category = session.query(Category).filter_by(name=category_name).first()
        if category:
            recipes = session.query(Recipe).filter_by(category_id = category.id).all()
            return recipes
        else:
            print("No such category exists.")
            return []
    

# Category class
class Category(Base):
    __tablename__ = 'categories'    

    id = Column(Integer(), primary_key=True)
    title = Column(String())

    recipes = relationship('Recipe', backref=backref('category')) 

    def __repr__(self):
        return f'Category: {self.title}'
    
    # Retrieve all categories
    @classmethod
    def all_categories(cls, session):
        categories = session.query(Category).all() 
        if categories:
            return categories
        else:
            return None

    # Add a new category
    @classmethod
    def add_category(cls, session, title):
        new_category = Category(title=title)
        session.add(new_category)
        session.commit()
        return new_category
    
    # Removing a category
    @classmethod
    def remove_category(cls, session, category_id):
        category = session.query(Category).filter_by(id=category_id).first()
        if category:
            session.delete(category)
            session.commit()
            print("Category deleted succesfully!")
            return category
        else:
            print("Category does not exist!")
            return None
        
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
        authors = session.query(Author).all()
        if authors:
            return authors
        else:
            print("No author")
            return None

    # Add an author
    @classmethod
    def add_author(cls, session, name):
        new_author = Author(name=name)
        session.add(new_author)
        session.commit()
        return new_author

    # Removing an author
    @classmethod
    def remove_author(cls, session, author_id):
        author = session.query(Author).filter_by(id=author_id).first()
        if author:
            session.delete(author)
            session.commit()
            print("Author deleted Succesfully!")
            return author
        else:
            print("Author does not exist")
            return None