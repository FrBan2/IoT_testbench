#The focus of this is to get a server client communication established
#where the client can send a message to a server and the server log
#the data in the most basic communication
#this is so we may troubleshoot the IOT Test bench communication and
#locate the problem of why its waiting for communication

import socket
import sys
import time
import datetime

#client ip address is 192.168.1.101
 
host  = ''
port  = 7005

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#bind socket to specified port
s.bind((host, port))

#listen for client only 1
s.listen(5)
#While istening print waiting then accept the
#connection and the client address
while True:
    print("Waiting for a connection ..")
    connection, client_address = s.accept()
    #print("done"+host +macaddr)
    
  
    

#attempt to connect with client
#and let the reader know its connected by printing the clients ip address
    #decode the data 
    try:
        data=connection.recv(1024)
        print('Connection established with', client_address)
        
        
        data = data.decode('utf-8')
        #data1= data.decode('utf-8')
        
        #print the data recieved by print str(data)
        #open a file to write data to and close it
        while True:  
                print(str(data),'\n',datetime.datetime.now().strftime("%m-%d-%Y-%H-%M-%S"))
                file = open("TestingCommunication.txt","w")
                file.write(data)
                file.write("\nIP Address")
                file.write(str(client_address))
                file.write("Date Recieved:")
                file.write(datetime.datetime.now().strftime("%m-%d-%Y-%H-%M-%S"))
                
                #print(str(file))
                file.close()
                
                break;
        #file.writelines(data)
    
    #connection.sendall(data)
    #print(%data,"Data has been sent ..")
    
    #try
    #data1 = data.decode
    finally:
        print 
        connection.close()
        print("Connection closed" )
    


#cnt = 0
#path = ('/home/pi/Desktop/'+'testRecieved' + str(cnt)+ '.doc')




