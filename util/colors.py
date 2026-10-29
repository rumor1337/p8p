import os

clear = '\033[H\033[2J'

white = '\033[1m'
reset = '\033[0m'

if os.name == 'nt':
    os.system('')

def clearScreen():
    print(clear)

def wrapColor(text, color=white):
    return f'{color}{text}{reset}'