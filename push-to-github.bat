@echo off
setlocal enabledelayedexpansion
title Push Smaran Raut SEO Website to GitHub

echo ======================================================================
echo   SMARAN RAUT SEO & WEB DEVELOPMENT - GITHUB REPOSITORY PUSHER
echo ======================================================================
echo.

cd /d "%~dp0"
echo Current Directory: %CD%
echo.

:: 1. Check if git is installed
where git >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo [ERROR] Git is not installed or not found in your system PATH.
    echo Please install Git from https://git-scm.com/downloads and try again.
    echo.
    pause
    exit /b 1
)

:: 2. Initialize git if not already initialized
if not exist ".git" (
    echo [1/5] Initializing Git repository...
    git init
) else (
    echo [1/5] Git repository already initialized.
)

:: 3. Stage all files
echo [2/5] Staging files...
git add .

:: 4. Commit
echo [3/5] Creating commit...
git commit -m "Initial commit: Smaran Raut SEO & Web Development Website" || (
    echo Note: Working tree clean or changes already committed.
)

:: 5. Set default branch to main
git branch -M main

:: 6. Check for remote or prompt user
git remote get-url origin >nul 2>&1
if %ERRORLEVEL% equ 0 (
    for /f "tokens=*" %%a in ('git remote get-url origin') do set REMOTE_URL=%%a
    echo.
    echo Existing remote 'origin' found: !REMOTE_URL!
    set /p USE_EXISTING="Do you want to push to this remote? (Y/N): "
    if /i "!USE_EXISTING!"=="Y" (
        goto PUSH_REPO
    )
    git remote remove origin
)

echo.
echo ======================================================================
echo Please create a new empty repository on GitHub:
echo 1. Open https://github.com/new in your browser
echo 2. Repository name: smaran-raut-seo (or any name you prefer)
echo 3. Leave it empty (DO NOT check "Add a README file")
echo 4. Click "Create repository"
echo ======================================================================
echo.
set /p REPO_URL="Paste your GitHub repository URL (e.g. https://github.com/username/smaran-raut-seo.git): "

if "%REPO_URL%"=="" (
    echo [ERROR] No URL entered. Aborted.
    pause
    exit /b 1
)

git remote add origin %REPO_URL%

:PUSH_REPO
echo.
echo [4/5] Pushing to GitHub (main branch)...
git push -u origin main

if %ERRORLEVEL% equ 0 (
    echo.
    echo ======================================================================
    echo [SUCCESS] Your website has been successfully pushed to GitHub!
    echo ======================================================================
) else (
    echo.
    echo [ERROR] Failed to push to GitHub.
    echo Please ensure you are authenticated or check your repository permissions.
)

echo.
pause
