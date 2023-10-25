@echo off

rem forcefully deletes pre-existing files
cd ".\Build"
for /F "delims=" %%i in ('dir /b') do (rmdir "%%i" /s/q || del "%%i" /s/q)

cd ".."

copy ".\star_setter_5.py" ".\Build"

cd ".\Build"

pyinstaller star_setter_5.py -y
rem timeout /t 10