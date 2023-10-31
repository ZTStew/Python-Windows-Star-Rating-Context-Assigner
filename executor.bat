rem @echo off

set LOGFILE=batch.log
call :LOG > %LOGFILE%
exit /B

:LOG
setlocal enabledelayedexpansion

rem Get the selected file's path from the command line argument (e.g., "%1")
set selected_file=%1
set rating=5

rem Loop through the command line arguments
:parse_args
if "%~1" == "--rating" (
  shift
  set rating=%~1
) else (
  rem Handle other arguments here if needed
)
timeout /t 10

echo "Selected File:"
echo %selected_file%

rem Call your Python script and pass the selected file as an argument
python "C:\Users\ZT\Documents\_) Programs\Batch-Programs\Python-Windows-Star-Rating-Context-Assigner\star_setter.py" --files "%selected_file%" --rating %rating%

timeout /t 10
echo "done"

pause

endlocal