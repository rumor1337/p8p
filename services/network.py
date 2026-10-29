import socket
import time
import os
import threading
from util.colors import wrapColor
from util.printHook import print
from services.transfer import receive

seenPeers = set()
syncInterval = 3
defaultPort = 8888
peers = {}

listenerSocket = None

def sendData(message, peerIp, command='chat:hi'):
	port = int(message.split(':')[2])
	listenerSocket.sendto(command.encode(), (peerIp, port))

def broadcast(identifier, port):
	udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	udpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

	while True:
		for targetPort in range(defaultPort, defaultPort + 16):
			for targetIp in ['127.0.0.1', '<broadcast>']:
				try:
					udpSocket.sendto(identifier.encode(), (targetIp, targetPort))
				except:
					pass
				
		time.sleep(syncInterval)

def replyTo(addr, command):
	listenerSocket.sendto(command.encode(), addr)

def listen(listener, identifier):
	global listenerSocket
	listenerSocket = listener
	while True:
		data, addr = listener.recvfrom(65535)
		message = data.decode()
		if message.startswith('p8p') and identifier not in message and message not in seenPeers:
			seenPeers.add(message)
			peers[message] = addr[0]

			print(wrapColor('located peer:'), f'{message}')
			sendData(message, peers[message])

		elif not message.startswith('p8p'):
			if message.startswith('chat'):
				message = message.split(':')[-1]
				print(wrapColor('received message:'), message)
			# [AI] couldn't find bug
			elif message.startswith('files'):
				print(wrapColor('peer dir:\n'), message.split(':', 1)[1])
			# [AI] couldn't find bug
			elif message.startswith('dir'):
				folder = message.split(':', 1)[1] or '.'
				if os.path.isdir(folder):
					replyTo(addr, 'files:' + ' ; '.join(f"[{'d' if os.path.isdir(os.path.join(folder, n)) else 'f'}] {n}" for n in os.listdir(folder)))
			elif message.startswith('dl'):
				fileName = message.split(':', 1)[1]
				if os.path.isdir(fileName):
					replyTo(addr, f'exists:{fileName}:0:dir')
				else:
					replyTo(addr, f'exists:{fileName}:{identifier.split(":")[-1]}:{os.path.exists(fileName)}')
			elif message.startswith('exists'):
				parts = message.split(':', 3)
				if len(parts) < 4:
					continue
				_, fileName, filePort, found = parts
				if found == 'True':
					threading.Thread(target=receive, args=(addr[0], int(filePort), fileName), daemon=True).start()
				elif found == 'dir':
					print(wrapColor('issue:'), f"{fileName} is a directory, you dummy; can't download that")
				else:
					print(wrapColor('issue:'), 'no such file?')