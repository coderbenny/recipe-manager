from lib.models import Author
import click

from ..main import session
# AUTHOR COMMANDS

@click.group()
def author_commands():
    pass

# Command for retrieving all authors
@author_commands.command()

def all_authors():
    authors = Author.all_authors(session)

    for author in authors:
        click.echo(author)

# Command for adding an author
@author_commands.command()
@click.argument('name')

def add_author(name):
    Author.add_author(session, name)
    click.echo(f'Author {name} added succesfully.')

# Command for removing an author
@author_commands.command()
@click.argument('author_id')

def remove_author(author_id):
    Author.remove_author(session, author_id)
    click.echo('Author removed successfully.')