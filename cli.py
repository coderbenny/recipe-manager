
import click
from db import session

from lib.models import Recipe, Author, Category


# Click command group
@click.group()
def cli():
    """Recipe Manager Application"""


@cli.command()
def all_authors():
    authors = Author.all_authors(session)

    for author in authors:
        click.echo(author)

# Command for adding an author
@cli.command()
@click.option('--name', prompt='Recipe Name', help='Name of the author')
def add_author(name):
    Author.add_author(session, name)
    click.echo(f'Author {name} added succesfully.')

# Command for removing an author
@cli.command()
@click.option('--author_id', prompt='Author Id', help='Author id')

def remove_author(author_id):
    Author.remove_author(session, author_id)
    click.echo('Author removed successfully.')


# Command for retrieving all categories
@cli.command()
def all_categories():
    categories = Category.all_categories(session)
    for category in categories:
        click.echo(category)


# Command for Adding a new category
@cli.command()
@click.option('--title', prompt='Category title', help='Name of the category')
# @click.argument('title')

def add_category(title):
    Category.add_category(session, title)
    click.echo(f'{title} category added successfully.')

# Command for removing a category
@cli.command()
@click.option('--category_id', prompt='Category Id', help='Id of the category', type=int)

def remove_category(category_id):
    Category.remove_category(category_id)
    click.echo('Category removed successfully.')


# Command to retrieve all recipes
@cli.command()
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
@click.option('--recipe_id', prompt='Recipe Id', help='Id of the recipe', type=int)
# @click.argument('recipe_id', type=int)

def remove_recipe(recipe_id):
    recipe = Recipe.remove_recipe(session, recipe_id)
    if recipe:
        click.echo(f'{recipe.name} removed successfully')

# Command to search for recipe by ingredient
@cli.command()
@click.option('--ingredient', prompt='Ingredient', help='Ingredient name')

def search_by_ingredient(ingredient):
    recipes = Recipe.search_by_ingredient(session, ingredient)
    for recipe in recipes:
        click.echo(recipe)

# Command to search for recipe by author name
@cli.command()
@click.option('--author_name', prompt='Author Name', help='Name of the author')

def search_by_author(author_name):
    recipes = Recipe.search_by_author(session, author_name)
    for recipe in recipes:
        click.echo(recipe)

# command to search for recipe by category name
@cli.command()
@click.option('--title', prompt='Category title', help='Title of the category')

def search_by_category(title):
    recipes = Recipe.search_by_category(session, title)
    for recipe in recipes:
        click.echo(recipe)


def submenu_return():
    """Return to the main menu."""
    return True


def execute_function(choice, options):
    """Execute Selected Functions Based On User Choice."""
    if choice == 13:
        return False
    elif choice == 14:
        return submenu_return()  # Go back to main menu

    # Get selected option
    selected_option = options.get(choice)

    # Check if selected option exists
    if selected_option:

        # Get selected function
        selected_function = selected_option["function"]

        # Check if function exists
        if selected_function:
            selected_function()
            return True
        else:
            click.echo("Exiting the program...")
            return False
    else:
        click.echo("Invalid choice. Please enter a valid option.")

    return True


def display_menu(options):
    """Display Menu Options."""
    click.echo("***Welcome to Recipe Manager CLI Application***")
    click.echo("Select an option: ")

    for i, option_data in options.items():
        text = option_data["text"]
        click.echo(f"{i}. {text}")


def display_submenu(submenu_options):
    """Display a Submenu."""
    click.echo("Select an option: ")
    for i, option_data in submenu_options.items():
        text = option_data["text"]
        click.echo(f"{i}. {text}")


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
    
    while True:
        display_menu(options)
        try:
            choice = click.prompt("Enter your choice", type=int)
        except click.ClickException:
            click.echo("Invalid input. Please enter an integer.")
            continue

        if not execute_function(choice, options):
            break

        # Allow returning to main menu
        if choice != 13:
            # Display submenu
            submenu_options = options.copy()
            submenu_options[14] = {"text": "Return to Main Menu", "function": None}
            display_submenu(submenu_options)
            try:
                submenu_choice = click.prompt("Enter your choice", type=int)
            except click.ClickException:
                click.echo("Invalid input. Please enter an integer.")
                continue

            if not execute_function(submenu_choice, submenu_options):
                break
