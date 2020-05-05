@echo off

REM check for python on machine
REM TODO: do this.

REM create venv and install packages
ECHO Creating Python Environment
call python -m venv venv
call .\venv\Scripts\activate.bat
call pip install -r requirements.txt

REM User params
call python install_helper.py

REM Create Task
ECHO Creating Scheduled Task
schtasks /Create /XML DoDuolingo_task_scheduler.xml /TN Duolingo\DoDuolingo
schtasks /Run /TN Duolingo\DoDuolingo

ECHO Deleting Scheduled Task XML File
del DoDuolingo_task_scheduler.xml

ECHO DONE!