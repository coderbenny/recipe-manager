import click
from lib.models import Author

from db import session


# AUTHOR COMMANDS

@click.group()
def author_commands():
    """Commands for Performing CRUD operations on Authors"""

# Command for retrieving all authors
@author_commands.command()
def all_authors():
    authors = Author.all_authors(session)

    for author in authors:
        click.echo(author)

# Command for adding an author
@author_commands.command()
@click.option('--name', prompt='Author name', help='Author name')

def add_author(name):
    Author.add_author(session, name)
    click.echo(f'Author {name} added succesfully.')

# Command for removing an author
@author_commands.command()
@click.option('--author_id', prompt='Author ID', help='Author Id')

def remove_author(author_id):
    Author.remove_author(session, author_id)
    click.echo('Author removed successfully.')