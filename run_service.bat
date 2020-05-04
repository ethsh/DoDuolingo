CD /d %~dp0

call .\venv\Scripts\activate.bat
call python main.py -n duolingo -u %1 -p %2 -t %3