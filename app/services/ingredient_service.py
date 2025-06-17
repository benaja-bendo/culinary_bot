# Business logic for ingredients and pantry items
from sqlalchemy.orm import Session
from app.models import Ingredient, PantryItem
from app.api.v1.schemas import IngredientCreate, PantryItemCreate

# def create_ingredient(db: Session, ingredient: IngredientCreate):
#     # db_ingredient = Ingredient(**ingredient.dict())
#     # db.add(db_ingredient)
#     # db.commit()
#     # db.refresh(db_ingredient)
#     # return db_ingredient
#     pass

# def add_pantry_item(db: Session, pantry_item: PantryItemCreate, user_id: int):
#     # db_pantry_item = PantryItem(**pantry_item.dict(), user_id=user_id)
#     # db.add(db_pantry_item)
#     # db.commit()
#     # db.refresh(db_pantry_item)
#     # return db_pantry_item
#     pass
