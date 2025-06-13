"""FastAPI routes."""

from __future__ import annotations

from fastapi import APIRouter, Depends, FastAPI
from pydantic import BaseModel
from sqlalchemy.orm import Session

from chef_ai.app.domain import models, services
from chef_ai.app.infrastructure.db import Database
from chef_ai.app.infrastructure.repositories import PantryRepository, RecipeRepository

router = APIRouter()

db = Database("sqlite:///chef.db")
db.create_tables()


def get_session() -> Session:
    with db.get_session() as session:
        yield session


class IngredientIn(BaseModel):
    name: str
    quantity: str
    category: str | None = None


class RecipeIn(BaseModel):
    name: str
    instructions: str
    tags: str | None = None
    ingredients: list[IngredientIn]


@router.post("/recipes")
def create_recipe(data: RecipeIn, session: Session = Depends(get_session)) -> dict:
    repo = RecipeRepository(session)
    ingredients = []
    for item in data.ingredients:
        ingredient = session.query(models.Ingredient).filter_by(name=item.name).first()
        if not ingredient:
            ingredient = models.Ingredient(name=item.name, category=item.category)
        ingredients.append(
            models.RecipeIngredient(ingredient=ingredient, quantity=item.quantity)
        )
    recipe = models.Recipe(
        name=data.name, instructions=data.instructions, tags=data.tags or "", ingredients=ingredients
    )
    repo.add(recipe)
    return {"id": recipe.id}


@router.get("/recipes")
def list_recipes(session: Session = Depends(get_session)) -> list[dict]:
    repo = RecipeRepository(session)
    return [
        {"id": r.id, "name": r.name, "tags": r.tags.split(",") if r.tags else []}
        for r in repo.list()
    ]


@router.post("/plan")
def plan_week(session: Session = Depends(get_session)) -> list[dict]:
    repo = RecipeRepository(session)
    recipes = repo.list()
    plan = services.build_weekly_plan(list(recipes))
    return [{"id": r.id, "name": r.name} for r in plan]


@router.get("/suggest")
def suggest(session: Session = Depends(get_session)) -> list[dict]:
    recipe_repo = RecipeRepository(session)
    pantry_repo = PantryRepository(session)
    suggestions = services.suggest_recipes_from_pantry(recipe_repo.list(), pantry_repo.list())
    return [{"id": r.id, "name": r.name} for r in suggestions]
