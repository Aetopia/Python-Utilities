# Python Utilities
A GitHub Repository where I store any Python Utilities I make.

## TUI Explorer
A Text User Interface Based File Explorer.

TUI Explorer allows one to access their operating's system file system via a shell.

![image](https://user-images.githubusercontent.com/41850963/154413904-bc885f1c-8f94-4973-9e6b-08373bdffa29.png)



### Commands:
```
Go <Folder> # Go to specified folder.
Back # Go one folder up.
Run <Arguments> # Run a program/shell command.
Exit # Exit TUI Explorer.
```


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
# Flags
ArgsSupport=False

Arguments=sys.argv[2:len(sys.argv)]
Args={}
for Index in range(len(Arguments)):
    Args[Index]=Arguments[Index]
if len(sys.argv) == 1: 
    code.InteractiveConsole().interact(banner=
    "Lightweight Python Environment\n", 
    exitmsg="")
elif len(sys.argv) == 2:
    runpy.run_path(sys.argv[1])
else:
    if ArgsSupport is True:
        print("Warning: 'sys.argv' & 'argparse' might likely not work correctly.\n")
        runpy.run_path(sys.argv[1], Args)  
```    

#### Requirements to Build:
1. Install Python `3.10`.
2. Run:
```ps
pip install nuitka
pip install zstandard
```
3. Run `build.bat`

**Note: Your compiled LPE will include the Python installation present on your device.**

