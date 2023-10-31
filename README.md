# Star Rating Context Assigner
---
## Description:  
Program is designed to be embedded into Window's Right-Click context menu to allow the user to quickly set the Star rating of a file
Currently, only .mp3 files are supported

---
### Usage:
(explanation of how to use the program)
1. In the Windows registry, `Computer\HKEY_CLASSES_ROOT\*\shell\`
2. Right click "shell", "New >", "Key"
3. The name of they key is what will be found in the context menu
4. Right click the new key that was just made and select, "New >", "Key" and name the key "command"
5. In command, double click "Default" and under "Value data:" enter: `C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe -ExecutionPolicy Bypass -File "[path to exe file]\run_star_setter.ps1" "%1" -rating [0-5]`
6. Create a new shell key for each rating level (6)
7. Under "Value data" set -rating to the desired rating level (0-5)
6. When right clicking files via file explorer, the new key(s) will appear in the context menu. Clicking them will run the program

---
### Notes:
Failed attempts to make program only show up when right clicking .mp3 files
Computer\HKEY_CLASSES_ROOT\.mp3
Computer\HKEY_CLASSES_ROOT\.mp3\shell\☼ mp31\command
Computer\HKEY_CLASSES_ROOT\*\shell
Computer\HKEY_CLASSES_ROOT\mp3file\shell\test\command

https://stackoverflow.com/questions/2123762/add-menu-item-to-windows-context-menu-only-for-specific-filetype
