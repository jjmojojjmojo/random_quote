#!/bin/bash
# script that creates a clone and does the init stuff from the guide

rm -rf random_quote
git clone random_quote_remote random_quote
cd random_quote
python -m venv .
./bin/pip install -r requirements.txt
./bin/pip install -e .
./bin/python scripts/generate_quotes.py
./bin/python scripts/init_workspace_db.py