#!usr/bin/python

import msvcrt
import os
import sys
import socket
import struct
import select

print('Welcome to the first iteration of secure chats')

username = str(input('Please enter a username to use: '))

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
host = 'localhost'
port = 5555
if(len(sys.argv) >= 2):
    port = int(sys.argv[1])
listener.bind((host, port))
listener.listen(5)

remotehost = 'localhost'
remoteport = 5555
if(len(sys.argv) >= 3):
    port = int(sys.argv[2])

remote = socket.socket()

print('Setup complete. Anything you type will be directly transmitted to the remote client')
outdata = ''
render = True

while True:
    readable, writeable, exception = select.select( [listener], [], [], 0)
    if(len(readable) != 0):
        (serversocket, address) = listener.accept();
        inname = struct.unpack('64s', serversocket.recv(64))[0].replace(b'\0',b'')
        insize = struct.unpack('I', serversocket.recv(4))[0]
        indata = struct.unpack('%ds' % insize, serversocket.recv(insize))[0]
        serversocket.close();

        print('\r[%s]: %s' % (inname.decode(), indata.decode()),end="\n",flush=True)
        render = True
    while msvcrt.kbhit():
        key = msvcrt.getch();
        char = ''
        try:
            char = key.decode();
        except UnicodeDecodeError:
            continue;

        if(key == b'\r'):
            outsize = len(outdata)

            remote.connect((remotehost, port))
            remote.send(struct.pack("64s", username.encode()))
            remote.send(struct.pack("I", outsize))
            remote.send(struct.pack('%ds' % outsize, outdata.encode()))
            remote.close()

            remote = socket.socket()

            outdata = ''
            print('\n',end="", flush=True)
            render = True

        elif(key == b'\x08'):
            print('\b \b',end="",flush=True)
            outdata = outdata[:-1]
            render = True

        else:
            outdata += char
            render = True

    if(render):
        print('\r[%s]:' % username, outdata,end="",flush=True)
        render = False
