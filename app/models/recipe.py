from sqlalchemy import Column, Integer, String, JSON, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base

class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    instructions = Column(String, nullable=False)
    ingredients = Column(JSON) # Structure: [{"ingredient_id": X, "quantity": Y, "unit": "Z"}] or similar
    tags = Column(JSON) # List of strings
    calories = Column(Integer)
    author_id = Column(Integer, ForeignKey("users.id"), nullable=True) # Assuming recipes can be standard or user-generated

    author = relationship("User") # Relationship to User (optional if we don't need to query recipes by author often)
    meal_plans = relationship("MealPlan", back_populates="recipe")
