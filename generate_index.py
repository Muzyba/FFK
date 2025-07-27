name: Generate index.html

on:
  push:
    branches:
      - main  # Lub inna twoja gałąź

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repo
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.x'

    - name: Run generate_index.py
      run: python generate_index.py

    - name: Commit and push changes
      run: |
        git config user.name "github-actions"
        git config user.email "github-actions@github.com"
        git add index.html
        git commit -m "Auto-update index.html" || echo "No changes to commit"
        git push
