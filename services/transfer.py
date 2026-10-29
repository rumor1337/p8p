import os
import shutil
import socket
import threading

from util.printHook import print
from util.colors import wrapColor

def serve(listener):
	while True:
		conn, addr = listener.accept()
		threading.Thread(target=handle, args=(conn,), daemon=True).start()

def handle(conn):
	fileName = conn.makefile('r').readline().strip()
	try:
		with open(fileName, 'rb') as f, conn.makefile('wb') as out:
			shutil.copyfileobj(f, out)
	except FileNotFoundError:
		print(wrapColor('issue:'), f'peer wanted missing file: {fileName}')
	conn.close()

def receive(peerIp, filePort, fileName):
	conn = socket.create_connection((peerIp, filePort))
	conn.sendall(fileName.encode() + b'\n')
	target = f'dl_{os.path.basename(fileName)}'
	with open(target, 'wb') as f, conn.makefile('rb') as src:
		shutil.copyfileobj(src, f)
	conn.close()
	print(wrapColor('downloaded:'), target)
