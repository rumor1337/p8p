import socket
import time
import os
from util.colors import wrapColor
from util.printHook import print

seenPeers = set()
syncInterval = 3
defaultPort = 8888
peers = {}

def sendData(message, peerIp, command='chat:hi'):
	port = int(message.split(':')[-1])
	udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	# allFiles = '\n'.join(os.listdir('.'))
	# udpSocket.sendto(f'dir:{allFiles}'.encode(), (peerIp, port))
	# print(wrapColor(f'sent message to peer at:'), f'{peerIp}:{port}')
	udpSocket.sendto(command.encode(), (peerIp, port))

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
	requester = next((ident for ident, ip in peers.items() if ip == addr[0]), None)
	if requester:
		sendData(requester, addr[0], command)

def listen(listener, identifier):
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
				replyTo(addr, f'exists:{os.path.exists(message.split(":", 1)[1])}')
			elif message.startswith('exists'):
				if message.split(':', 1)[1] == 'True':
					print('yes, exists')
				else:
					print(wrapColor('issue:'), 'no such file?')