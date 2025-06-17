"""Data repositories."""

from __future__ import annotations

from collections.abc import Iterable

from sqlalchemy.orm import Session

from chef_ai.app.domain import models


class RecipeRepository:
    """Repository for recipes."""

    def __init__(self, session: Session) -> None:
        self.session = session

    def add(self, recipe: models.Recipe) -> None:
        self.session.add(recipe)
        self.session.commit()

    def get(self, recipe_id: int) -> models.Recipe | None:
        return self.session.get(models.Recipe, recipe_id)

    def list(self) -> Iterable[models.Recipe]:
        return self.session.query(models.Recipe).all()


class PantryRepository:
    """Repository for pantry items."""

    def __init__(self, session: Session) -> None:
        self.session = session

    def upsert(self, item: models.PantryItem) -> None:
        existing = self.session.get(models.PantryItem, item.ingredient_id)
        if existing:
            existing.quantity = item.quantity
        else:
            self.session.add(item)
        self.session.commit()

    def list(self) -> Iterable[models.PantryItem]:
        return self.session.query(models.PantryItem).all()
