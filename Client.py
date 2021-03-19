import socket
import sys
import os
import art
import argparse
import time

#Special Vars
usrinrun = False
PACKETSIZE = 6048
doto = False

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

art.tprint('Rabbit')

##args
parser = argparse.ArgumentParser()
parser.add_argument('-host', help='Specify Host', required=True)
parser.add_argument('-port', help='Specify Port', default='40966')
parser.add_argument('--vidf', help="Specify 'video command' file", default='vidcmd.txt')
args = parser.parse_args()

#args
vidc = args.vidf

##socks
clients = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Host and Port
host = args.host
port = args.port
#Connect
try:
    #Indicate and Connect
    print('Connecting to ' + host + ':' + port)
    clients.connect((str(host), int(port)))
    usrinrun = True
except:
    print(colors.RED + 'Failed to connect, the following could be the problem:')
    print('Failed to connect to server')
    print('Server not up')

print(colors.BOLD + colors.GREEN + 'Ready For User Input' + colors.END)

##User input
def main():
    while usrinrun == True:
        doto = True
        try:
            while doto == True:
                msg = input(colors.BOLD + colors.CYAN + 'Rabbit → ' + colors.END)
                doto = False
                if not msg:
                    print('Please Enter A String')
                    doto = True
            clients.send(msg.encode('UTF-8'))
            if msg == 'getvid':
                print('Opening Video Client')
                time.sleep(1)
                with open(str(vidc), 'r') as f:
                    vidcmd = f.read()
                os.system(str(vidcmd))
            returned = clients.recv(PACKETSIZE).decode('UTF-8')
            datatopcov = print(colors.BOLD + colors.BLUE + '-------------------------')
            data = print(colors.YELLOW + returned)
            databotcov = print(colors.BOLD + colors.BLUE + '-------------------------')
        except:
            print(colors.RED + 'Failed to contact/receive from the server')
            break
main()