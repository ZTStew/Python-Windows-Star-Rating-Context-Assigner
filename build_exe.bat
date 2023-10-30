@echo off

rem forcefully deletes pre-existing files
cd ".\Build"
for /F "delims=" %%i in ('dir /b') do (rmdir "%%i" /s/q || del "%%i" /s/q)

rem navigates back to base directory
cd ".."

rem copies python program over to different folder to build it
copy ".\star_setter_0.py" ".\Build"
copy ".\star_setter_1.py" ".\Build"
copy ".\star_setter_2.py" ".\Build"
copy ".\star_setter_3.py" ".\Build"
copy ".\star_setter_4.py" ".\Build"
copy ".\star_setter_5.py" ".\Build"
copy ".\star_setter.py" ".\Build"
copy ".\execute.py" ".\Build"

rem moves to location of copied file
cd ".\Build"

rem builds python program into .exe
pyinstaller --noconsole star_setter_0.py -y
pyinstaller --noconsole star_setter_1.py -y
pyinstaller --noconsole star_setter_2.py -y
pyinstaller --noconsole star_setter_3.py -y
pyinstaller --noconsole star_setter_4.py -y
pyinstaller --noconsole star_setter_5.py -y
pyinstaller --noconsole star_setter.py -y
rem timeout /t 10