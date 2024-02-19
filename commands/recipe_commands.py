from lib.models import Recipe

import click

from ..main import session


# RECIPE COMMANDS

@click.group()
def recipe_commands():
    pass

# Command to retrieve all recipes
@recipe_commands.command()
def all_recipes():
    recipes = Recipe.all_recipes(session)
    for recipe in recipes:
        click.echo(recipe)

# Command to create a recipe
@recipe_commands.command()
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
@recipe_commands.command() 
@click.argument('recipe_id', type=int)

def remove_recipe(recipe_id):
    recipe = Recipe.remove_recipe(session, recipe_id)
    if recipe:
        click.echo(f'{recipe.name} removed successfully')

# Command to search for recipe by ingredient
@recipe_commands.command()
@click.argument('ingredient')

def search_by_ingredient(ingredient):
    recipes = Recipe.search_by_ingredient(session, ingredient)
    for recipe in recipes:
        click.echo(recipe)

# Command to search for recipe by author name
@recipe_commands.command()
@click.argument('author_name')

def search_by_author(author_name):
    recipes = Recipe.search_by_author(session, author_name)
    for recipe in recipes:
        click.echo(recipe)

# command to search for recipe by category name
@recipe_commands.command()
@click.argument('category_name')

def search_by_category(category_name):
    recipes = Recipe.search_by_category(session, category_name)
    for recipe in recipes:
        click.echo(recipe)
