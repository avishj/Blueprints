set dotenv-load

default:
    @just --list

lint:
    uv run ruff check --show-fixes --statistics .
    uv run ruff format --check .

lint-fix:
    uv run ruff check --fix .
    uv run ruff format .

typecheck:
    uv run ty check src/ tests/

test *args:
    uv run pytest -n auto {{ args }}

cov:
    uv run pytest --cov --cov-report=term --cov-report=html --cov-report=xml --cov-fail-under=70 --junitxml=results.xml -n auto

complexity:
    uv run complexipy src/ --max-complexity 15

semgrep:
    uv run semgrep scan --config=auto .

build:
    uv build

docs:
    uv run mkdocs serve

docs-build:
    uv run mkdocs build --strict

ci: lint typecheck cov complexity semgrep

clean:
    rm -rf build/ dist/ *.egg-info/ .pytest_cache/ .ruff_cache/ .coverage htmlcov/ coverage.xml results.xml site/ .ty/
