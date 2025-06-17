"""ASGI application."""

from fastapi import FastAPI

from chef_ai.app.interface.api.routes import router

app = FastAPI(title="ChefAI")
app.include_router(router)
