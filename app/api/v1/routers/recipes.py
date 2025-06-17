from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.api.v1.schemas.recipe_schema import Recipe, RecipeCreate
# Import service functions (e.g., create_recipe, get_recipe, get_recipes) from app.services.recipe_service
# For now, we'll alias it to avoid import errors for commented out code
import app.services.recipe_service as services
from app.db.session import get_db

router = APIRouter()

# @router.post("/", response_model=Recipe)
# def create_new_recipe(recipe: RecipeCreate, db: Session = Depends(get_db)):
#     # return services.create_recipe(db=db, recipe=recipe)
#     pass

# @router.get("/{recipe_id}", response_model=Recipe)
# def read_recipe(recipe_id: int, db: Session = Depends(get_db)):
#     # db_recipe = services.get_recipe(db, recipe_id=recipe_id)
#     # if db_recipe is None:
#     #     raise HTTPException(status_code=404, detail="Recipe not found")
#     # return db_recipe
#     pass

# @router.get("/", response_model=List[Recipe])
# def read_recipes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     # recipes = services.get_recipes(db, skip=skip, limit=limit)
#     # return recipes
#     pass
