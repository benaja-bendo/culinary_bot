"""Typer CLI commands."""

from __future__ import annotations

import typer
from tabulate import tabulate

from chef_ai.app.domain import models, services
from chef_ai.app.infrastructure.db import Database
from chef_ai.app.infrastructure.repositories import PantryRepository, RecipeRepository

app = typer.Typer()

db = Database("sqlite:///chef.db")
db.create_tables()


@app.command()
def add_recipe(name: str, instructions: str) -> None:
    """Add a recipe interactively."""
    with db.get_session() as session:
        repo = RecipeRepository(session)
        ingredients: list[models.RecipeIngredient] = []
        while True:
            ing = typer.prompt("Ingredient (blank to finish)")
            if not ing:
                break
            qty = typer.prompt("Quantity")
            ingredient = session.query(models.Ingredient).filter_by(name=ing).first()
            if not ingredient:
                ingredient = models.Ingredient(name=ing)
            ingredients.append(models.RecipeIngredient(ingredient=ingredient, quantity=qty))
        recipe = models.Recipe(name=name, instructions=instructions, ingredients=ingredients)
        repo.add(recipe)
        typer.echo(f"Added recipe {recipe.id}")


@app.command()
def list_recipes() -> None:
    """List recipes."""
    with db.get_session() as session:
        repo = RecipeRepository(session)
        table = [(r.id, r.name) for r in repo.list()]
        typer.echo(tabulate(table, headers=["id", "name"]))


@app.command()
def plan_week() -> None:
    """Generate a weekly meal plan."""
    with db.get_session() as session:
        repo = RecipeRepository(session)
        plan = services.build_weekly_plan(list(repo.list()))
        table = [(r.id, r.name) for r in plan]
        typer.echo(tabulate(table, headers=["id", "name"]))
        shopping = services.compute_shopping_list(plan)
        typer.echo("\nShopping list:")
        for cat, items in shopping.items():
            typer.echo(f"## {cat}")
            for i in items:
                typer.echo(f"- {i}")
