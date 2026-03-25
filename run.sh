#!/bin/bash

# Ultimate Planner Helper Script (Enterprise Edition)
# Usage: ./run.sh [command]

if [ -d "venv" ]; then
    PYTHON="./venv/bin/python"
    echo "Using virtual environment: venv"
else
    PYTHON="python3"
    echo "Using system python: python3"
fi

COMMAND=$1

case $COMMAND in
    "run")
        $PYTHON manage.py runserver
        ;;
    "migrate")
        $PYTHON manage.py migrate
        ;;
    "makemigrations")
        $PYTHON manage.py makemigrations
        ;;
    "test")
        $PYTHON manage.py test professionals
        ;;
    "check")
        $PYTHON manage.py check
        ;;
    "shell")
        $PYTHON manage.py shell
        ;;
    "seed")
        $PYTHON manage.py loaddata apps/professionals/fixtures/seed.json
        ;;
    *)
        echo "Usage: ./run.sh {run|migrate|makemigrations|test|check|shell}"
        exit 1
        ;;
esac
