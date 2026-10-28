import socket
import threading
import sys
import os
import time

syncInterval = 3

defaultPort = 8888

def checkPort(port: int):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

def broadcast(identifier, port):
    udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    while True:
        for targetPort in range(defaultPort, defaultPort + 16):
            udpSocket.sendto(identifier.encode(), ('<broadcast>', targetPort))
        time.sleep(syncInterval)

def listen(listener, identifier):
    seenPeers = set()

    while True:
        data, addr = listener.recvfrom(1024)
        message = data.decode()
        if identifier not in message and message not in seenPeers:
            seenPeers.add(message)
            print(f'located peer {message}')

def main():
    listener = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    port = defaultPort
    while True:
        try:
            listener.bind(('0.0.0.0', port))
            break
        except:
            port += 1

    identifier = f'p8p:{socket.gethostname()}:{port}'
    print('started..')

    threading.Thread(target=broadcast, args=(identifier, port), daemon=True).start()
    threading.Thread(target=listen, args=(listener, identifier), daemon=True).start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print('exiting')
        sys.exit(0)

if __name__ == '__main__':
    main()

