from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.db.session import Base

class PantryItem(Base):
    __tablename__ = "pantry_items"

    id = Column(Integer, primary_key=True, index=True) # Added a primary key for PantryItem
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    ingredient_id = Column(Integer, ForeignKey("ingredients.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    unit = Column(String, nullable=False)
    expires_on = Column(Date, nullable=True)

    owner = relationship("User", back_populates="pantry_items")
    ingredient_info = relationship("Ingredient", back_populates="pantry_items")
