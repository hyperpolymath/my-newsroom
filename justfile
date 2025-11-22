# Justfile for My-newsroom
# Build automation and developer workflows

# Default recipe (show help)
default:
    @just --list

# Install Python development dependencies
install:
    pip install -e .
    pip install -r requirements-dev.txt

# Run all Python tests
test:
    pytest tests/ -v

# Run tests with coverage
test-cov:
    pytest tests/ -v --cov=mynewsroom --cov-report=term --cov-report=html

# Run tests in parallel
test-parallel:
    pytest tests/ -v -n auto

# Run property-based tests only
test-property:
    pytest tests/ -v -m property --hypothesis-show-statistics

# Run linting checks
lint:
    ruff check src/ tests/
    black --check src/ tests/
    mypy src/

# Auto-fix linting issues
lint-fix:
    ruff check --fix src/ tests/
    black src/ tests/

# Type check with mypy
typecheck:
    mypy src/ --strict

# Security scanning
security:
    safety check -r requirements.txt -r requirements-dev.txt
    bandit -r src/

# Validate RSR compliance
validate:
    @echo "Checking RSR Bronze level compliance..."
    @test -f README.md || (echo "❌ README.md missing" && exit 1)
    @test -f LICENSE.txt || (echo "❌ LICENSE.txt missing" && exit 1)
    @test -f SECURITY.md || (echo "❌ SECURITY.md missing" && exit 1)
    @test -f CONTRIBUTING.md || (echo "❌ CONTRIBUTING.md missing" && exit 1)
    @test -f CODE_OF_CONDUCT.md || (echo "❌ CODE_OF_CONDUCT.md missing" && exit 1)
    @test -f .well-known/security.txt || (echo "❌ security.txt missing" && exit 1)
    @test -f .well-known/ai.txt || (echo "❌ ai.txt missing" && exit 1)
    @test -f .well-known/humans.txt || (echo "❌ humans.txt missing" && exit 1)
    @echo "✅ RSR Bronze level requirements met"

# Build Python package
build-python:
    python -m build

# Build Rust Solo compiler (when available)
build-rust:
    cargo build --release

# Build all components
build: build-python
    @echo "✅ Python package built"

# Clean build artifacts
clean:
    rm -rf build/ dist/ *.egg-info
    rm -rf target/
    rm -rf htmlcov/ .coverage
    rm -rf .pytest_cache/ .mypy_cache/ .ruff_cache/
    find . -type d -name __pycache__ -exec rm -rf {} +

# Run examples
examples:
    @echo "Running Python examples..."
    python examples/dempster_shafer_basic.py

# Generate documentation
docs:
    mkdocs build

# Serve documentation locally
docs-serve:
    mkdocs serve

# Full CI pipeline (local)
ci: lint test-cov security validate build
    @echo "✅ Full CI pipeline passed"

# Quick check before commit
pre-commit: lint-fix test
    @echo "✅ Ready to commit"

# Run benchmark tests
bench:
    pytest tests/ -v -m benchmark --benchmark-only

# Profile code performance
profile:
    python -m cProfile -o profile.stats examples/dempster_shafer_basic.py
    python -m pstats profile.stats

# Check code complexity
complexity:
    radon cc src/ -a -nb
    radon mi src/ -nb

# Count lines of code
loc:
    @echo "=== Lines of Code ==="
    @find src/ -name "*.py" | xargs wc -l | tail -1
    @echo ""
    @find tests/ -name "*.py" | xargs wc -l | tail -1

# Git pre-push hook
pre-push: ci
    @echo "✅ Ready to push"

# Install git hooks
install-hooks:
    echo "#!/bin/sh\njust pre-commit" > .git/hooks/pre-commit
    chmod +x .git/hooks/pre-commit
    echo "#!/bin/sh\njust pre-push" > .git/hooks/pre-push
    chmod +x .git/hooks/pre-push
    @echo "✅ Git hooks installed"
