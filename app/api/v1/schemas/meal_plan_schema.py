from pydantic import BaseModel
from datetime import date
from typing import Optional

class MealPlanBase(BaseModel):
    date: date
    recipe_id: int
    status: Optional[str] = "PLANNED"

class MealPlanCreate(MealPlanBase):
    pass

class MealPlan(MealPlanBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
