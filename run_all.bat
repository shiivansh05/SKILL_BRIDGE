@echo off
echo ========================================================
echo   SkillBridge Enterprise - Launching Backend & Frontend
echo ========================================================
echo.
start "SkillBridge Backend API (Port 5000)" cmd /k "%~dp0run_backend.bat"
timeout /t 2 /nobreak >nul
start "SkillBridge Frontend (Port 8000)" cmd /k "%~dp0run_frontend.bat"
