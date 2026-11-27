# List the available receipes
default:
    @just --list

# Run ruff and ty
check:
    uv run ruff check .
    uv run ruff format --check .
    uv run ty check

# Fix lint issues and format code
fix:
    uv run ruff check --fix .
    uv run ruff format .

# Run ty type checker
ty:
    uv run ty check

# Runthe API with auto-reload
dev:
    uv run fastapi dev
