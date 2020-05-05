@echo off
REM check for python on machine

REM User params
call python install_helper.py

REM Create Task
ECHO Creating Scheduled Task
schtasks /Create /XML DoDuolingo_task_scheduler.xml /TN Duolingo\DoDuolingo
schtasks /Run /TN Duolingo\DoDuolingo

ECHO Deleting Scheduled Task XML File
del DoDuolingo_task_scheduler.xml

ECHO DONE!