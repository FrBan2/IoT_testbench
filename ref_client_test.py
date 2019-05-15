#this is the client portion of the testing
#this will send a message to the server
#the server will recieve and log the data
#this is in conjucntion with testing the communication
#between the server client of the IOT test bench 

import socket
import re
from uuid import getnode as get_mac


#host of server and communication port being used
#headers = 'Connection:keep-alive\r\n'
host = '192.168.1.101'
port= 8000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
mac = get_mac
mac_addr=(':'.join(re.findall('..', '%012x'% get_mac())))

#mac_n=str(mac_addr)
s.connect((host,port))

while s.connect:
    #data=s.recv(1024)
    #print("Recieved",data)
    #s.connect((host,port))
 
    #interations=["first","second", "

    #for x in interations:
    #get all three interations of the message to send and store to the file in the server 
    try:
        #mac=get_mac()
        
        message=('Refrigerator, In Use,'+str(mac_addr).upper())
        #mac=str.encode(mac,'utf-8'))
        print(message)
        s.send(message.encode('utf-8'))
        #s.send(encode(mac,'utp-8'))
        #headers
        break
        #figure out how to send mac address now that ive pulled it from the client
    except socket.error:
        print("Binding Failed ..")
        #sys.exit()
        s.close()
    

#finally:
#    print("Closing socket")
#def mac_addr(connection):
    #while True:
        #data1= conn.recv(1024)
    #if data1 
   
#s.close()

#print("Sock has been bounded ..")
#print("Socket is ?,