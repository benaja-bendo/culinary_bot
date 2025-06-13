"""Domain models using SQLAlchemy ORM."""

from __future__ import annotations

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    """Base class for declarative models."""


class Recipe(Base):
    """A cooking recipe."""

    __tablename__ = "recipes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    instructions: Mapped[str] = mapped_column(String, nullable=False)
    tags: Mapped[str] = mapped_column(String, default="")

    ingredients: Mapped[list[RecipeIngredient]] = relationship(
        back_populates="recipe", cascade="all, delete-orphan"
    )


class Ingredient(Base):
    """An ingredient with an optional category for shopping list grouping."""

    __tablename__ = "ingredients"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    category: Mapped[str | None] = mapped_column(String, nullable=True)

    recipes: Mapped[list[RecipeIngredient]] = relationship(back_populates="ingredient")


class RecipeIngredient(Base):
    """Association table between recipes and ingredients."""

    __tablename__ = "recipe_ingredients"

    recipe_id: Mapped[int] = mapped_column(
        ForeignKey("recipes.id"), primary_key=True
    )
    ingredient_id: Mapped[int] = mapped_column(
        ForeignKey("ingredients.id"), primary_key=True
    )
    quantity: Mapped[str] = mapped_column(String, nullable=False)

    recipe: Mapped[Recipe] = relationship(back_populates="ingredients")
    ingredient: Mapped[Ingredient] = relationship(back_populates="recipes")


class PantryItem(Base):
    """Ingredient available in the user's pantry."""

    __tablename__ = "pantry"

    ingredient_id: Mapped[int] = mapped_column(
        ForeignKey("ingredients.id"), primary_key=True
    )
    quantity: Mapped[str] = mapped_column(String, nullable=False)

    ingredient: Mapped[Ingredient] = relationship()
