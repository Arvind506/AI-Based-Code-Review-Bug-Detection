@echo off
echo Starting AI Code Review Assistant...
cd /d "%~dp0"
call .venv\Scripts\activate.bat
streamlit run app.py
pause
