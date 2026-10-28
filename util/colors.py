import os

white = '\033[1m'
reset = '\033[0m'

if os.name == 'nt':
    os.system('')

def wrapColor(text, color=white):
    return f'{color}{text}{reset}'