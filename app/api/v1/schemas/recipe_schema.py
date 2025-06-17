from pydantic import BaseModel
from typing import Optional, List, Any

class RecipeBase(BaseModel):
    name: str
    instructions: str
    ingredients: List[Any] # Example: [{"ingredient_id": 1, "name": "Tomato", "quantity": 2, "unit": "pcs"}]
    tags: Optional[List[str]] = None
    calories: Optional[int] = None

class RecipeCreate(RecipeBase):
    pass

class Recipe(RecipeBase):
    id: int
    author_id: Optional[int] = None

    class Config:
        orm_mode = True
