@echo off
py -OO -m nuitka --onefile --standalone --follow-imports LPE.py --output-dir="%TEMP%" -o "LPE.exe"
timeout 5
