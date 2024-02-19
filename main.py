from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import click

from lib.models import Base, Recipe, Author, Category


engine = create_engine('sqlite:///recipes.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


# Click command group
@click.group()
def cli():
    pass

# Function to display menu options
def display_menu(options):
    click.echo("***Welcome to Recipe Manager CLI Application***")
    click.echo("Select an option: ")

    for i, option in enumerate(options, 1):
        click.echo(f"{i}. {option}")



# RECIPE COMMANDS

# Command to retrieve all recipes
def all_recipes():
    recipes = Recipe.all_recipes(session)
    for recipe in recipes:
        click.echo(recipe)

# Command to create a recipe
@cli.command()
@click.option('--name', prompt='Recipe Name', help='Name of the recipe')
@click.option('--ingredients', prompt='Ingredients', help='Ingredients of the recipe')
@click.option('--instructions', prompt='Instructions', help='Instructions for making the recipe')
@click.option('--category', prompt='Category', help='Category of the recipe')
@click.option('--author', prompt='Author', help='Author of the recipe')

def create_recipe(name, ingredients, instructions, category, author):
    category_obj = Category.add_category(session, category)
    author_obj = Author.add_author(session, author)
    Recipe.create_recipe(session, name, ingredients, instructions, category_obj.id, author_obj.id)
    click.echo(f'{name} recipe added successfully')


# Command to remove a recipe
@cli.command() 
@click.argument('recipe_id', type=int)

def remove_recipe(recipe_id):
    recipe = Recipe.remove_recipe(session, recipe_id)
    if recipe:
        click.echo(f'{recipe.name} removed successfully')

# Command to search for recipe by ingredient
@cli.command()
@click.argument('ingredient')

def search_by_ingredient(ingredient):
    recipes = Recipe.search_by_ingredient(session, ingredient)
    for recipe in recipes:
        click.echo(recipe)

# Command to search for recipe by author name
@cli.command()
@click.argument('author_name')

def search_by_author(author_name):
    recipes = Recipe.search_by_author(session, author_name)
    for recipe in recipes:
        click.echo(recipe)

# command to search for recipe by category name
@cli.command()
@click.argument('category_name')

def search_by_category(category_name):
    recipes = Recipe.search_by_category(session, category_name)
    for recipe in recipes:
        click.echo(recipe)


# CATEGORY COMMANDS

# Command for retrieving all categories
@cli.command()

def all_categories():
    categories = Category.all_categories(session)
    for category in categories:
        click.echo(category)


# Command for Adding a new category
@cli.command()
@click.argument('title')

def add_category(title):
    Category.add_category(session, title)
    click.echo(f'{title} category added successfully.')

# Command for removing a category
@cli.command()
@click.argument('category_id')

def remove_category(category_id):
    Category.remove_category(category_id)
    click.echo('Category removed successfully.')


# AUTHOR COMMANDS

# Command for retrieving all authors
@cli.command()

def all_authors():
    authors = Author.all_authors(session)

    for author in authors:
        click.echo(author)

# Command for adding an author
@cli.command()
@click.argument('name')

def add_author(name):
    Author.add_author(session, name)
    click.echo(f'Author {name} added succesfully.')

# Command for removing an author
@cli.command()
@click.argument('author_id')

def remove_author(author_id):
    Author.remove_author(session, author_id)
    click.echo('Author removed successfully.')


if __name__ == '__main__':
    
    # Options for the user
    options = {
        1: {"text": "List all recipes", "function": all_recipes},
        2: {"text": "Add a recipe", "function": create_recipe},
        3: {"text": "Remove a recipe", "function": remove_recipe},
        4: {"text": "Search recipes by ingredients", "function": search_by_ingredient},
        5: {"text": "Search recipes by author", "function": search_by_author},
        6: {"text": "Search recipes by category", "function": search_by_category},
        7: {"text": "List all categories", "function": all_categories},
        8: {"text": "Add a category", "function": add_category},
        9: {"text": "Remove a category", "function": remove_category},
        10: {"text": "List all authors", "function": all_authors},
        11: {"text": "Add an author", "function": add_author},
        12: {"text": "Remove an author", "function": remove_author},
        13: {"text": "Exit", "function": None}
    }


    # Funct
    def execute_function(choice, options):
        if choice == 13:
            return False

        # Get selected option
        selected_option = options.get(choice)
        
        # Check if selected option exists
        if selected_option:

            # Get selected function
            selected_function = selected_option["function"]
            
            # Check if function exists
            if selected_function:
                selected_function()
            else:
                click.echo("Exiting the program...")
                return False
        else:
            click.echo("Invalid choice. Please enter a valid option.")

        return True


    while True:
        display_menu(options)
        try:
            choice = click.prompt("Enter your choice", type=int)
        except click.ClickException:
            click.echo("Invalid input. Please enter an integer.")
            continue

        if not execute_function(choice, options):
            break

        
