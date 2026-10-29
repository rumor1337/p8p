import socket
import threading
import sys

from util.printHook import print, input
from services.network import defaultPort, broadcast, listen
from services.transfer import serve
from services.commands import run

def main():
	listener = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	port = defaultPort
	while True:
		try:
			listener.bind(('0.0.0.0', port))
			break
		except:
			port += 1

	fileListener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	filePort = defaultPort
	while True:
		try:
			fileListener.bind(('0.0.0.0', filePort))
			fileListener.listen()
			break
		except:
			filePort += 1

	identifier = f'p8p:{socket.gethostname()}:{port}:{filePort}'
	print('started p8p, hold your horses')

	threading.Thread(target=broadcast, args=(identifier, port), daemon=True).start()
	threading.Thread(target=listen, args=(listener, identifier), daemon=True).start()
	threading.Thread(target=serve, args=(fileListener,), daemon=True).start()

	try:
		while True:
			run(input('> '))
	except KeyboardInterrupt:
		print('\nexiting')
		sys.exit(0)

if __name__ == '__main__':
	main()

