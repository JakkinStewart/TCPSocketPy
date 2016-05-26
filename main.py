#! /usr/bin/env python
# Written by Joshua Jordi

import os

try:
    for i in range(1024, 6000):
        os.system("python tcpServer.py %i" % i)

except KeyboardInterrupt:
    exit()
