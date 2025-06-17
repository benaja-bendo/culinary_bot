from pydantic import BaseModel
from typing import Optional

class IngredientBase(BaseModel):
    name: str
    category: Optional[str] = None
    unit_default: Optional[str] = None

class IngredientCreate(IngredientBase):
    pass

class Ingredient(IngredientBase):
    id: int

    class Config:
        orm_mode = True
