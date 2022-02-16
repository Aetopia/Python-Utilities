# Modules
from glob import glob
from os import getcwd, system, path, chdir
from subprocess import run
from fnmatch import filter

# UI 
class UI:
    def Line(Character):
        for _ in range(100): print(Character, end='')
        print()                   

# Explorer
def Explorer():
    print('\n TUI Explorer')
    UI.Line('_')
    if str(glob('*')) != '[]':
        for Item in glob("*"):
            Whitespaces=''
            if path.isfile(path.abspath(Item)): 
                Type=f'{path.splitext(Item)[1].title()} File'
                Icon = '#'
            elif path.isdir(path.abspath(Item)):
                Type='File Folder'  
                Icon = '>' 
            if len(Item) > 50: Item=f'{Item[:50]}...'
            elif len(Item) < 50:
                Length=53-len(Item)
                for _ in range(Length):
                    Whitespaces+=" "
                Output=f"{Icon} {Item}{Whitespaces} | {Type}"
            else: Output=f"{Icon} {Item}"
            Whitespaces=''
            print(Output)
    else: print('~ |Empty Directory|')           
    UI.Line('‾')    
    print(f'Path: {getcwd()}')
    print(""" ________________________        
| Go | Back | Run | Exit |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾""")

# Toolbar
def Toolbar():
    Command = input("Toolbar > ").split(' ',1)
    match Command[0].lower():
        case 'go':
            Folder = None
            try:
                for Folder in (filter(glob('*'),f'{Command[1]}*')):
                    if path.isdir(path.abspath(Folder)):
                        Folder = Folder
                        break
                if Folder is None: Folder = Command[1]
            except: pass
            try: chdir(path.abspath(Folder))
            except: pass
        case 'back': chdir(path.abspath(path.dirname(getcwd())))
        case 'run': 
            try: run(Command[1],shell=True)
            except: pass
        case 'exit':
            try: system('cls')
            except: system('clear') 
            exit()
     
# Main
if __name__ == '__main__':
    while True:
        try: system('cls')
        except: system('clear')    
        Explorer()
        try:Toolbar()
        except KeyboardInterrupt as Error:
            if str(Error) == "<class 'KeyboardInterrupt'>": pass     
