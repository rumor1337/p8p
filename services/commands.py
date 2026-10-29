from services.network import sendData, peers
from util.printHook import print
from util.colors import wrapColor

def chat(message):
    if not peers:
        print(wrapColor('issue:'), 'hold up, buster; noone is there')
        return
    for identifier, ip in peers.items():
        sendData(identifier, ip, command=message)

def help(message):
    print(wrapColor('no can do, sorry'))
    print(wrapColor('maybe try:'))
    for command in commands:
      print(command)

commands = {'/chat': chat, '/help': help}

def run(line):
    parts = line.split(' ', 1)
    handler = commands.get(parts[0])
    if handler:
        handler(parts[1] if len(parts) > 1 else '')
    else:
        print(wrapColor('issue:'), 'what command are you even referencing?')