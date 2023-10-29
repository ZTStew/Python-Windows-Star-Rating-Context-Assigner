# Star Rating Context Assigner
---
## Description:  
Program is designed to be embedded into Window's Right-Click context menu to allow the user to quickly set the Star rating of a file
Currently, only .mp3 files are supported

---
### Usage:
(explanation of how to use the program)
1. Run `pyinstaller star_setter_x.py` to create .exe files
2. In the Windows registry, `Computer\HKEY_CLASSES_ROOT\*\shell\`
3. Right click "shell", "New >", "Key"
4. The name of they key is what will be found in the context menu
5. Right click the new key that was just made and select, "New >", "Key" and name the key "command"
6. In command, double click "Default" and under "Value data:" enter: `"[path to exe file].exe" "%1"`
7. When right clicking files via file explorer, the new key will appear in the context menu
8. Select the key's name select, "More Apps ↓" then "Look for more apps on this PC". Pick the program's .exe file
