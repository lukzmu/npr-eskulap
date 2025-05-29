#!/bin/bash
set -e

if [ "$1" = 'runserver' ]; then
    shift
    cd src
    uv run python -m pelican -lr content -s core/settings.py -o output -b 0.0.0.0 --ignore-cache $@
elif [ "$1" = 'lint' ]; then
    shift
    OPTS=${@:-'.'}
    echo "-- ruff lint --" && uv run ruff check $OPTS || EXIT=$?
    echo "-- ruff format --" && uv run ruff format --check $OPTS || EXIT=$?
    MYPY_OPTS=${@:-'src/'}
    echo "-- mypy --" && uv run mypy $MYPY_OPTS || EXIT=$?
    exit ${EXIT:-0}
elif [ "$1" = 'fmt' ]; then
    shift
    OPTS=${@:-'.'}
    echo "-- ruff lint --" && uv run ruff check --fix $OPTS
    echo "-- ruff format --" && uv run ruff format $OPTS
    exit 0
elif [ "$1" = 'test' ]; then
    shift
    OPTS=${@:-'src/'}
    echo "-- bandit --" && uv run bandit -r $OPTS
    echo "-- pytest --" && uv run pytest --cov=src --cov-report=json
fi

exec "$@"