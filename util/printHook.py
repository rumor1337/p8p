import threading
from util.colors import clearScreen

textHistory = []
inputText = '> '
lock = threading.Lock()

builtInPrint = print
builtInInput = input

def redraw():
    clearScreen()
    for line in textHistory:
        builtInPrint(line)
    builtInPrint(inputText, end='', flush=True)

def print(*args, **kwargs):
	sep = kwargs.get('sep', ' ')
	msg = sep.join(str(arg) for arg in args)

	with lock:
		textHistory.append(msg)
		redraw()

def input(prompt=''):
	global inputText
	if prompt:
		inputText = prompt

	with lock:
		redraw()

	res = builtInInput('')
	with lock:
		redraw()

	return res