"""Domain services implementing business logic."""

from __future__ import annotations

import random
from collections import defaultdict
from collections.abc import Iterable

from chef_ai.app.domain import models


def suggest_recipes_from_pantry(
    recipes: Iterable[models.Recipe], pantry: Iterable[models.PantryItem]
) -> list[models.Recipe]:
    """Return recipes that can be cooked from pantry ingredients."""
    available = {item.ingredient_id for item in pantry}
    result = []
    for recipe in recipes:
        if all(ri.ingredient_id in available for ri in recipe.ingredients):
            result.append(recipe)
    return result


def build_weekly_plan(recipes: list[models.Recipe], days: int = 7) -> list[models.Recipe]:
    """Return a weekly plan of recipes."""
    if not recipes:
        return []
    return [random.choice(recipes) for _ in range(days)]


def compute_shopping_list(plan: Iterable[models.Recipe]) -> dict[str, list[str]]:
    """Aggregate ingredients needed for recipes grouped by category."""
    shopping: dict[str, list[str]] = defaultdict(list)
    for recipe in plan:
        for ri in recipe.ingredients:
            category = ri.ingredient.category or "misc"
            shopping[category].append(f"{ri.quantity} {ri.ingredient.name}")
    return shopping
