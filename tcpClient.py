#! /usr/bin/env python
# Written by Joshua Jordi

import socket
import sys
import subprocess

sock = socket.socket()

serverAddress = ('localhost', 80)

sock.connect(serverAddress)
message = subprocess.check_output("wget -q -O - http://ip.tupeux.com | tail", shell=True)

sock.sendall(str(message).encode("utf-8"))

sock.close()
