from .user import User
from .recipe import Recipe
from .ingredient import Ingredient
from .pantry_item import PantryItem
from .meal_plan import MealPlan
from app.db.session import Base, engine

# Create all tables in the database.
# This is suitable for development environments.
# For production, you might want to use Alembic for migrations.
Base.metadata.create_all(bind=engine)
