#this is the client portion of the testing
#this will send a message to the server
#the server will recieve and log the data
#this is in conjucntion with testing the communication
#between the server client of the IOT test bench 


import socket
from uuid import getnode as get_mac


#host of server and communication port being used
host = '192.168.1.103'
port = 7005
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host,port))
mac = get_mac()

mac_n=str(mac)
interations=["first","second", "third"]
for x in interations:
#get all three interations of the message to send and store to the file in the server 
    try:
    #mac=get_mac()
        message =('Communication testing:'+x +'\n\tFrom MAC Address:'+mac_n)
    #mac=str.encode(mac,'utf-8'))
        print("Sending ", message,"\n")
        s.sendall(message.encode('utf-8'))
    #s.send(mac.encode('utf-8)) 
    #figure out how to send mac address now that ive pulled it from the client
    except socket.error:
        print("Binding Failed ..")
        sys.exit()
        s.close()


#finally:
#    print("Closing socket")
#def mac_addr(connection):
    #while True;
    #data1= conn.recv(1024)
    #if data = mac:
s.close()

#print("Sock has been bounded ..")
#print("Socket is 