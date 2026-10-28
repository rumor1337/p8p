import socket
import time
from util.colors import wrapColor

seenPeers = set()
syncInterval = 3
defaultPort = 8888
peers = {}

def sendData(message, peerIp):
        port = int(message.split(':')[-1])
        udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udpSocket.sendto('sending straight packets, straight bytes jit'.encode(), (peerIp, port))
        print(wrapColor(f'sent message to peer at:'), f'{peerIp}:{port}')

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

def listen(listener, identifier):
    while True:
        data, addr = listener.recvfrom(1024)
        message = data.decode()
        if message.startswith('p8p') and identifier not in message and message not in seenPeers:
            seenPeers.add(message)
            print(wrapColor('located peer:'), f'{message}')
            sendData(message, addr[0])
        elif not message.startswith('p8p'):
            print(wrapColor('received message:'), message)