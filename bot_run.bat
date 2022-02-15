@echo off

call %~dp0PB/Scripts/activate

cd %~dp0

python bot.py

pause 