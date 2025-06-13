# ChefAI

ChefAI is a recipe recommender and weekly-meal planner.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
```

## Run API

```bash
uvicorn chef_ai.app:app --reload
```

## Run CLI

```bash
python -m chef_ai.main
```

## Lint

```bash
ruff check .
```

## Test

```bash
pytest
```
