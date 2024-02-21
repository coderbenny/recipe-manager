# Use the cli.py as my app's entry point

import click
from db import session

from functions.recipe_functions import recipe_commands
from functions.category_functions import category_commands
from functions.author_functions import author_commands


# Click command group
@click.group()
def cli():
    """Recipe Manager Application"""

# Adding the sub-commands to the cli command group
cli.add_command(recipe_commands)
cli.add_command(category_commands)
cli.add_command(author_commands)


# Function to display menu options
def display_menu(options):
    """Display Menu Options"""
    click.echo("***Welcome to Recipe Manager CLI Application***")
    click.echo("Select an option: ")

    for i, option_data in options.items():
        text = option_data["text"]
        click.echo(f"{i}. {text}")

# Function to execute selected function based on user choice
def execute_function(choice, options):
    """Execute Selected Functions Based On User Choice"""
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


if __name__ == '__main__':
    
    # Options for the user
    options = {
        1: {"text": "List all recipes", "function": recipe_commands.all_recipes},
        2: {"text": "Add a recipe", "function": recipe_commands.create_recipe},
        3: {"text": "Remove a recipe", "function": recipe_commands.remove_recipe},
        4: {"text": "Search recipes by ingredients", "function": recipe_commands.search_by_ingredient},
        5: {"text": "Search recipes by author", "function": recipe_commands.search_by_author},
        6: {"text": "Search recipes by category", "function": recipe_commands.search_by_category},
        7: {"text": "List all categories", "function": category_commands.all_categories},
        8: {"text": "Add a category", "function": category_commands.add_category},
        9: {"text": "Remove a category", "function": category_commands.remove_category},
        10: {"text": "List all authors", "function": author_commands.all_authors},
        11: {"text": "Add an author", "function": author_commands.add_author},
        12: {"text": "Remove an author", "function": author_commands.remove_author},
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
