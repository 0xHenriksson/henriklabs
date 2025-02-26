#!/bin/bash
set -e

# Change to the repository root directory
cd "$(dirname "$0")/.."

# Run tests with coverage
pytest --cov=app --cov=config tests/

# Format the code (if --format is passed)
if [ "$1" == "--format" ]; then
    echo "Formatting code..."
    black app/ config/ tests/
    isort app/ config/ tests/
fi

# Run linting (if --lint is passed)
if [ "$1" == "--lint" ] || [ "$2" == "--lint" ]; then
    echo "Running linters..."
    ruff check app/ config/ tests/
    mypy app/ config/ tests/
fi