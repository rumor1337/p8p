import socket
import threading
import sys
import os
import time

syncInterval = 3

port = 8888

port = int(input(f'enter connect port (or default to {port}): ') or port)
identifier = f'p8p:{socket.gethostname()}:{port}'

target = int(input(f'enter peer ip: '))
targetPort = int(input(f'enter peer conn port (or default to {port}): ') or port)

def checkPort(port: int):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

def broadcast():
    udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    while True:
        udpSocket.sendto(identifier.encode(), ('255.255.255.255', port))
        time.sleep(syncInterval)

def listen():
    listener = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    listener.bind(('0.0.0.0', port))
    while True:
        data, addr = listener.recvfrom(1024)
        message = data.decode()
        if identifier not in message:
            print('located peer')

threading.Thread(target=broadcast, daemon=True).start()
threading.Thread(target=listen, daemon=True).start()

try:
    while True:
        time.sleep(0.5)
except:
    print('an exception has occured')
