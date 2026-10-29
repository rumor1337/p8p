import socket
import time
import os
from util.colors import wrapColor
from util.printHook import print

seenPeers = set()
syncInterval = 3
defaultPort = 8888
peers = {}

def sendData(message, peerIp, command='hi'):
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

def listen(listener, identifier):
    while True:
        data, addr = listener.recvfrom(1024)
        message = data.decode()
        if message.startswith('p8p') and identifier not in message and message not in seenPeers:
            seenPeers.add(message)
            peers[message] = addr[0]

            print(wrapColor('located peer:'), f'{message}')
            sendData(message, peers[message])

        elif not message.startswith('p8p'):
            # if message.startswith('dir'):
            #     files = message.split(':')[-1]
            #     print(wrapColor(f'recieved all downloadable things:\n'), files)
            #     input('choose file number: ')
            # else:
            print(wrapColor('received message:'), message)