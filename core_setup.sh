#!/bin/bash

# Create the project root directory
mkdir recipe_suggestion_app
cd recipe_suggestion_app

# Create main app file
touch app.py

# Create requirements.txt and README.md
touch requirements.txt
touch README.md

# Create .env file with Streamlit license key placeholder
echo "STREAMLIT_LICENSE_KEY=your_streamlit_license_key_here" > .env

# Create src directory and __init__.py
mkdir src
touch src/__init__.py

# Create class files in src directory
touch src/ingredient.py
touch src/recipe.py
touch src/recipe_api_client.py
touch src/user_session.py
touch src/data_manager.py  # Optional
touch src/app_ui.py

# Create data directory (optional)
mkdir data

# Create tests directory (optional)
mkdir tests
touch tests/__init__.py

echo "Project directory structure created successfully, including .env file."
