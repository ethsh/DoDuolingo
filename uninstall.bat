@echo off

ECHO Deactivating python venv
call .\venv\Scripts\deactivate.bat

ECHO Deleting Scheduled Task
schtasks /Delete /TN Duolingo\DoDuolingo