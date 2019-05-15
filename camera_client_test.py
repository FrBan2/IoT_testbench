#this is the client portion of the testing
#this will send a message to the server
#the server will recieve and log the data
#this is in conjucntion with testing the communication
#between the server client of the IOT test bench 

import socket
import re
from uuid import getnode as get_mac



host = '192.168.1.101'
port= 8000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
mac = get_mac
mac_addr=(':'.join(re.findall('..', '%012x'% get_mac())))

#mac_n=str(mac_addr)
s.connect((host,port))

while s.connect:
    
    try:
        #mac=get_mac()
        
        message=('Camera, In Use,'+str(mac_addr).upper())
        
        print(message)
        s.send(message.encode('utf-8'))
        
        break
       
    except socket.error:
        print("Binding Failed ..")
        #sys.exit()
        s.close()
    

