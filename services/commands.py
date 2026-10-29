from services.network import sendData, peers
from util.printHook import print
from util.colors import wrapColor

def missingPeer():
    print(wrapColor('issue:'), 'hold up, buster; noone is there')

def chat(message):
	if not peers:
		missingPeer()
		return
	for identifier, ip in list(peers.items()):
		sendData(identifier, ip, f'chat:{message}')

def help(message):
	print(wrapColor('no can do, sorry'))
	print(wrapColor('maybe try:'))
	for command in commands:
		if command != "/help":
		    print(command)

def download(fileName):
	if not peers:
		missingPeer()
		return
	for identifier, ip in list(peers.items()):
		sendData(identifier, ip, f'dl:{fileName}')

def dir(message):
	if not peers:
		missingPeer()
		return
	for identifier, ip in list(peers.items()):
		sendData(identifier, ip, f'dir:{message}')
		

commands = {'/chat': chat, '/help': help, '/download': download, '/dir': dir}

def run(line):
	parts = line.split(' ', 1)
	handler = commands.get(parts[0])
	if handler:
		handler(parts[1] if len(parts) > 1 else '')
	else:
		print(wrapColor('issue:'), 'what command are you even referencing?')