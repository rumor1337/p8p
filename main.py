import socket
import threading
import sys
import os
import time


seenPeers = set()
syncInterval = 3

blue = '\033[1;34m'
reset = '\033[0m'

defaultPort = 8888

# idk why, truly but windows needs this?
if os.name == 'nt':
    os.system('')

def wrapColor(text, color=blue):
    return f'{color}{text}{reset}'

def checkPort(port: int):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

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
            
def sendData(message, peerIp):
        port = int(message.split(':')[-1])
        udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udpSocket.sendto('sending straight packets, straight bytes jit'.encode(), (peerIp, port))
        print(f'sent message to peer at {peerIp}:{port}')

def main():
    listener = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    port = defaultPort
    while True:
        try:
            listener.bind(('0.0.0.0', port))
            break
        except:
            port += 1

    identifier = f'p8p:{socket.gethostname()}:{port}'
    print('started p8p, hold your horses')

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

