#!/bin/bash

# Define project root directory
PROJECT_ROOT="."

# Create main project structure
mkdir -p $PROJECT_ROOT/{app/routes,app/templates}

# Create essential files
touch $PROJECT_ROOT/{docker-compose.yml,Dockerfile,.env,requirements.txt,README.md}

# Create application files
touch $PROJECT_ROOT/app/{main.py,database.py,models.py,crud.py,schemas.py,background_tasks.py}

touch $PROJECT_ROOT/app/routes/{listings.py,map.py,food_finder.py}

touch $PROJECT_ROOT/app/templates/index.html

# Print success message
echo "Project structure generated successfully!"
