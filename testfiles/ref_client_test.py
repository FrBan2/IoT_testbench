import socket
import re
import datetime
import time
from uuid import getnode as get_mac
import random

# This is the refrigerator client portion still in testing
# this current program has set hours of activity with randomized minutes and seconds

h = ["07", "07", "08", "08", "08", "08", "15", "15",
     "16", "16", "17", "17", "17", "17", "18", "18"]

for h in h:

    host = '192.168.1.100'
    port = 8000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 5)
    mac = get_mac
    mac_addr = (':'.join(re.findall('..', '%012x' % get_mac())))

    s.connect((host, port))

    min = str(random.randint(0, 60)).zfill(2)
    sec = str(random.randint(0, 60)).zfill(2)

    message = ('Refrigerator,In Use,'+str(mac_addr).upper()+',' +
               datetime.datetime.now().strftime("%m-%d-%Y")+'-'+str(h)+'-'+(min)+'-'+(sec)+";")
    print(message)

    s.sendall(message.encode("utf-8"))

    time.sleep(2)

s.close()

