start:
	uv run python src/main.py

lintfix:
	uv run ruff format .
	uv run ruff check . --fix

lint:
	uv run ruff check .

lintwatch:
	uv run ruff check . --watch

typecheck:
	uv run pyright