from fastapi import FastAPI
# Import routers once they are defined with actual routes
from app.api.v1.routers import chat, recipes, pantry, planner # These are modules
from app.db.session import engine #, init_db # init_db can be called here or in models.__init__
from app.models import Base # Import Base to ensure models are known to SQLAlchemy if not using init_db from models

# Call init_db here if you prefer explicit initialization,
# especially if models.__init__.py doesn't call Base.metadata.create_all(bind=engine)
# For this setup, models.__init__.py already calls it.
# If it didn't, you would uncomment the next line:
# Base.metadata.create_all(bind=engine)
# or call a dedicated init_db() function from app.db.session if you created one that does this.

app = FastAPI(title="Cooking Chatbot API", version="0.1.0")

# Include routers from API v1
app.include_router(chat.router, prefix="/api/v1/chat", tags=["Chat"])
app.include_router(recipes.router, prefix="/api/v1/recipes", tags=["Recipes"])
app.include_router(pantry.router, prefix="/api/v1/pantry", tags=["Pantry"])
app.include_router(planner.router, prefix="/api/v1/planner", tags=["Planner"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Cooking Chatbot API!"}

# Optional: Add startup event to create DB tables if not handled by models.__init__
# @app.on_event("startup")
# def on_startup():
#     # This ensures tables are created when the app starts
#     # init_db() # Assuming init_db from app.db.session creates tables
#     # or:
#     # Base.metadata.create_all(bind=engine)
#     pass
