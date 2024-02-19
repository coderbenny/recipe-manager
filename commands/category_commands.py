from lib.models import Category

import click

from ..main import session

# CATEGORY COMMANDS

@click.group()
def category_commands():
    pass

# Command for retrieving all categories
@category_commands.command()
def all_categories():
    categories = Category.all_categories(session)
    for category in categories:
        click.echo(category)


# Command for Adding a new category
@category_commands.command()
@click.argument('title')

def add_category(title):
    Category.add_category(session, title)
    click.echo(f'{title} category added successfully.')

# Command for removing a category
@category_commands.command()
@click.argument('category_id')

def remove_category(category_id):
    Category.remove_category(category_id)
    click.echo('Category removed successfully.')

