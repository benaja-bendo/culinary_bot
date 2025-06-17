from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.session import Base

class Ingredient(Base):
    __tablename__ = "ingredients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    category = Column(String, index=True)
    unit_default = Column(String) # Default unit like 'g', 'ml', 'pcs'

    pantry_items = relationship("PantryItem", back_populates="ingredient_info")
