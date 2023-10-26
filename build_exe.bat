@echo off

rem forcefully deletes pre-existing files
cd ".\Build"
for /F "delims=" %%i in ('dir /b') do (rmdir "%%i" /s/q || del "%%i" /s/q)

rem navigates back to base directory
cd ".."

rem copies python program over to different folder to build it
copy ".\star_setter_5.py" ".\Build"

rem moves to location of copied file
cd ".\Build"

rem builds python program into .exe
pyinstaller star_setter_5.py -y
rem timeout /t 10