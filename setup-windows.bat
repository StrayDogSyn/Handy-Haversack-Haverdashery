@echo off
echo ================================================
echo Handy Haversack Haverdashery - Quick Setup
echo ================================================
echo.

echo [1/4] Setting up Backend...
cd backend

echo Creating virtual environment...
python -m venv venv

echo Activating virtual environment...
call venv\Scripts\activate

echo Installing dependencies...
pip install -r requirements.txt

echo Creating .env file...
if not exist .env (
    copy .env.example .env
    echo Created .env file
) else (
    echo .env file already exists
)

cd ..

echo.
echo [2/4] Setting up Frontend...
cd frontend

echo Installing npm dependencies...
call npm install

cd ..

echo.
echo [3/4] Creating data directories...
if not exist data\sqlite mkdir data\sqlite
if not exist data\json mkdir data\json
if not exist data\pdfs mkdir data\pdfs

echo.
echo [4/4] Setup Complete!
echo.
echo ================================================
echo Next Steps:
echo ================================================
echo.
echo 1. Open TWO terminal windows
echo.
echo 2. Terminal 1 - Backend:
echo    cd backend
echo    venv\Scripts\activate
echo    uvicorn app.main:app --reload
echo.
echo 3. Terminal 2 - Frontend:
echo    cd frontend
echo    npm start
echo.
echo 4. Open browser to:
echo    Frontend: http://localhost:3000
echo    API Docs: http://localhost:8000/docs
echo.
echo ================================================
echo Happy rolling! 🎲
echo ================================================
pause
