from pydantic import BaseModel
from typing import Optional
from datetime import date

class PantryItemBase(BaseModel):
    ingredient_id: int
    quantity: int
    unit: str
    expires_on: Optional[date] = None

class PantryItemCreate(PantryItemBase):
    pass

class PantryItem(PantryItemBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
