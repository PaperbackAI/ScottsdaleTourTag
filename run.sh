#!/bin/bash

# Ensure the script stops on errors
set -e

# Build and start the Docker containers
echo "Starting the application..."
docker-compose up --build
