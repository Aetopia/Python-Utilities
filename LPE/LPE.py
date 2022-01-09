import sys
import runpy
import code
if len(sys.argv) == 1: 
    code.InteractiveConsole().interact(banner="Lightweight Python Environment: Python 3.9.9\n", exitmsg="")
try:
    runpy.run_path(sys.argv[1])
except:
    pass    