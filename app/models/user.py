from sqlalchemy import Column, Integer, String, JSON, DateTime
from sqlalchemy.orm import relationship
from app.db.session import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    prefs = Column(JSON)  # For allergies, régimes, unités
    created_at = Column(DateTime, default=datetime.utcnow)

    pantry_items = relationship("PantryItem", back_populates="owner")
    meal_plans = relationship("MealPlan", back_populates="user")
