from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.db.session import Base

class MealPlan(Base):
    __tablename__ = "meal_plans"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    date = Column(Date, nullable=False)
    recipe_id = Column(Integer, ForeignKey("recipes.id"), nullable=False)
    status = Column(String, default="PLANNED") # PLANNED, COOKED, SKIPPED

    user = relationship("User", back_populates="meal_plans")
    recipe = relationship("Recipe", back_populates="meal_plans")
