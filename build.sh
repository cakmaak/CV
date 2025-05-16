#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

# Add the project directory to PYTHONPATH
export PYTHONPATH=$PYTHONPATH:$(pwd)

# Collect static files
python cvsite/manage.py collectstatic --no-input

# Run migrations
python cvsite/manage.py migrate 