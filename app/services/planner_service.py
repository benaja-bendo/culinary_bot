# Business logic for meal planning
from sqlalchemy.orm import Session
from app.models import MealPlan
from app.api.v1.schemas import MealPlanCreate

# def create_meal_plan_entry(db: Session, meal_plan: MealPlanCreate, user_id: int):
#     # db_meal_plan = MealPlan(**meal_plan.dict(), user_id=user_id)
#     # db.add(db_meal_plan)
#     # db.commit()
#     # db.refresh(db_meal_plan)
#     # return db_meal_plan
#     pass
