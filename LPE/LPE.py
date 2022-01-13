import sys
import runpy
import code
# Flags
ArgsSupport=False # Enables (sys.argv) & (argparse) Support.

Arguments=sys.argv[2:len(sys.argv)]
Args={}
for Index in range(len(Arguments)):
    Args[Index]=Arguments[Index]
if len(sys.argv) == 1: 
    code.InteractiveConsole().interact(banner=
    "Lightweight Python Environment: Python 3.9.9\n", 
    exitmsg="")
elif len(sys.argv) == 2:
    runpy.run_path(sys.argv[1])
else:
    if ArgsSupport is True:
        print("Warning: 'sys.argv' & 'argparse' might likely not work correctly.\n")
        runpy.run_path(sys.argv[1], Args)
