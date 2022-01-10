# Python Utilities
A GitHub Repository where I store any Python Utilities I make.

## Lightweight Python Environment
This is a simple Python script which allows you to run a full python installation but as a small package.       

You can also import custom modules installed via `pip` and include them in your LPE.
```py
#------------
import module1
import module2
#-------------
import sys
import runpy
import code
if len(sys.argv) == 1: 
    code.InteractiveConsole().interact(banner="Lightweight Python Environment\n", exitmsg="")
try:
    runpy.run_path(sys.argv[1])
except:
    pass    
```    

#### Requirements to Build:
1. Install Python `3.9`.
2. Run:
```ps
pip install nuitka
pip install zstandard
```
3. Run `build.bat`

**Note: Your compiled LPE will include the python installation present on your device.**

