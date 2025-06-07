#!/bin/bash
echo "Setting up Contact Management App..."

# Create virtual environment
python3 -m venv venv
echo "Virtual environment created."

# Activate virtual environment
source venv/bin/activate
echo "Virtual environment activated."

# Install dependencies
pip install -r requirements.txt
echo "Dependencies installed."

# Run migrations
python manage.py migrate
echo "Database migrations applied."

echo ""
echo "Setup completed! To run the app:"
echo "1. Activate the virtual environment: source venv/bin/activate"
echo "2. Run the server: python manage.py runserver"
echo "3. Access the app at http://localhost:8000"
echo "" 