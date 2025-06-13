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
python chef_ai/main.py
```

## Lint

```bash
ruff .
```

## Test

```bash
pytest
```
