# help-alura-agents

Playground for experimenting with LangChain, LangGraph and Google Gemini.

## Stack

- Python 3.13+ with [uv](https://docs.astral.sh/uv/)
- `langchain` + `langchain-google-genai` (Gemini 2.5 Flash)
- `langgraph`, `pydantic`, `pydantic-settings`
- Ruff for lint/format, Pyright for typechecking

## Setup

```bash
uv sync
cp .env.example .env   # add your GEMINI_API_KEY
```

## Run

```bash
make start             # uv run python src/main.py
```

## Tasks

| Command | What it does |
| --- | --- |
| `make lint` | Ruff check |
| `make lintfix` | Ruff format + autofix |
| `make typecheck` | Pyright |
