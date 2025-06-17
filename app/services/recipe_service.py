# Business logic for recipes
from sqlalchemy.orm import Session
from app.models.recipe import Recipe
from app.api.v1.schemas.recipe_schema import RecipeCreate

# def get_recipe(db: Session, recipe_id: int):
#     # return db.query(Recipe).filter(Recipe.id == recipe_id).first()
#     pass

# def get_recipes(db: Session, skip: int = 0, limit: int = 100):
#     # return db.query(Recipe).offset(skip).limit(limit).all()
#     pass

# def create_recipe(db: Session, recipe: RecipeCreate, author_id: int = None):
#     # db_recipe = Recipe(**recipe.dict(), author_id=author_id)
#     # db.add(db_recipe)
#     # db.commit()
#     # db.refresh(db_recipe)
#     # return db_recipe
#     pass
