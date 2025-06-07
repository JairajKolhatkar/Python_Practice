@echo off
echo Setting up Contact Management App...

REM Create virtual environment
python -m venv venv
echo Virtual environment created.

REM Activate virtual environment
call venv\Scripts\activate.bat
echo Virtual environment activated.

REM Install dependencies
pip install -r requirements.txt
echo Dependencies installed.

REM Run migrations
python manage.py migrate
echo Database migrations applied.

echo.
echo Setup completed! To run the app:
echo 1. Activate the virtual environment: venv\Scripts\activate
echo 2. Run the server: python manage.py runserver
echo 3. Access the app at http://localhost:8000
echo.

pause 