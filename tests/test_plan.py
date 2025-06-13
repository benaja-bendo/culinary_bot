from chef_ai.app.domain import models, services


def sample_recipes():
    ing = models.Ingredient(name="Tomato")
    return [
        models.Recipe(
            name="R1",
            instructions="",
            ingredients=[models.RecipeIngredient(ingredient=ing, quantity="1")],
        ),
        models.Recipe(
            name="R2",
            instructions="",
            ingredients=[models.RecipeIngredient(ingredient=ing, quantity="2")],
        ),
    ]


def test_weekly_plan_length():
    plan = services.build_weekly_plan(sample_recipes(), days=7)
    assert len(plan) == 7


def test_shopping_list():
    recipes = sample_recipes()
    shopping = services.compute_shopping_list(recipes)
    assert "misc" in shopping
    assert any("Tomato" in item for item in shopping["misc"])
