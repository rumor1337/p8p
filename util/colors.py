import os

blue = '\033[1;34m'
reset = '\033[0m'

if os.name == 'nt':
    os.system('')

def wrapColor(text, color=blue):
    return f'{color}{text}{reset}'