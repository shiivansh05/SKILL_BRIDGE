@echo off
echo ========================================================
echo   SkillBridge Enterprise - Launching Frontend
echo ========================================================
echo.
echo Serving frontend at http://localhost:8000 ...
echo Press Ctrl+C in this window to stop the server.
echo.
start http://localhost:8000/
cd /d "%~dp0\frontend"
python -m http.server 8000
pause
