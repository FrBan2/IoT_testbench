#The focus of this is to get a server client communication established
#where the client can send a message to a server and the server log
#the data in the most basic communication
#this is so we may troubleshoot the IOT Test bench communication and
#locate the problem of why its waiting for communication
import multiprocessing 
import socket
import re
import sys
import time
import datetime
import sqlite3
#c.execute('''CREATE TABLE testing (Entry, Data, Client Address, Date Recieved)''')

#client ip address is 192.168.from sqlite3 import Error
 
host  = ''
port  = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#bind socket to specified port
s.bind((host, port))
s.listen(6)
count=0
print("Waiting for a connection ..")
conn=sqlite3.connect('/home/pi/Desktop/iot_test_bench/testfiles/testing.db')

#decode the data
while True:
    connection, address = s.accept()
    ip_address, port = str(address[0]), str(address[1])
    try:
        #print('Connection established with', address)
        data=connection.recv(1024)
        datadecode = data.decode('utf-8')
        array = datadecode.split(",")
        appliance, message, mac_address, datetime= str(array[0]), str(array[1]), str(array[2]), str(array[3])
        
        #if data:
        count=count+1
        c=conn.cursor()
        print(data)
        print("Connection Established with: ",ip_address,"\n Through port: ", port,"\n",appliance, "\n",message,"\n ",mac_address,"\n", datetime)
        print(' Data '+str(count))
        #file = open("/home/pi/Desktop/iot_test_bench/testfiles/TestingCommunication.txt","a")
        #c.execute('''CREATE TABLE testing (Date, Appliance, Message, Ip Address, Mac Address)''')
        print("Awaiting new data")
        c.execute("INSERT INTO testing VALUES (?,?,?,?,?)",(datetime, appliance, message, ip_address, mac_address))
        conn.commit()
        
    #while data:
        #file.write(datadecoded)
        #file.write("\nIP Address")
        #file.write(ip_address)
        #file.write("Date Recieved:")
        #file.write(datetime.datetime.now().strftime("%m-%d-%Y-%H-%M-%S"))
        #print(str(file))
        #file.close()
        #print("Awaiting new data")
        #reply = 'Recieved...' + str(data)
        #print('Returning Data to Client')
        #conn.send(reply)
    
    except socket.error:
        print("Connection Failed...")
        #file.close()
        conn.close()


