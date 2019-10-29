import socket
import re
from uuid import getnode as get_mac

# This is the general client portion of testing
# used to confirm communication through tcp/ip protocol.
# The server will recieve and log the data using SQLite.

port = 8000
host = '192.168.1.100'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mac = get_mac
mac_addr = (':'.join(re.findall('..', '%012x' % get_mac())))
s.connect((host, port))

while s.connect:
    try:
        message = ('Communication Test From Mac Address: ' +
                   str(mac_addr).upper())
        # mac=str.encode(mac,'utf-8'))
        print(message)
        s.send(message.encode('utf-8'))
        # s.send(encode(mac,'utp-8'))
        break

    except socket.error:
        print("Binding Failed ..")
        s.close()
