from chef_ai.app.domain import models, services
from chef_ai.app.infrastructure.db import Database
from chef_ai.app.infrastructure.repositories import RecipeRepository


def setup_db():
    db = Database("sqlite:///:memory:")
    db.create_tables()
    return db


def test_create_recipe_with_ingredients():
    db = setup_db()
    with db.get_session() as session:
        repo = RecipeRepository(session)
        ing = models.Ingredient(name="Tomato")
        recipe = models.Recipe(
            name="Salad", instructions="Mix", ingredients=[
                models.RecipeIngredient(ingredient=ing, quantity="2")
            ]
        )
        repo.add(recipe)
        assert recipe.id is not None
