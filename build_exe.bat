@echo off

copy ".\star_setter_5.py" ".\Build"

cd ".\Build"

pyinstaller star_setter_5.py
rem timeout /t 10