@echo off
title Smaran Raut SEO - Local Server (Port 8080)
cd /d "%~dp0"
echo ====================================================================
echo  Launching Smaran Raut SEO Local Production Server...
echo  Directory: %~dp0
echo  Local URL:  http://localhost:8080
echo ====================================================================

:: Automatically open default browser after a brief delay
start "" "http://localhost:8080"

:: Start the high-performance dual-stack python server
python server.py
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [Notice] Falling back to standard Python http.server on port 8080...
    python -m http.server 8080
)

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [Notice] Python not found in PATH. Opening pre-rendered site directly...
    start "" "%~dp0index.html"
)

pause
