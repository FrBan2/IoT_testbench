# The focus of this is to get a server client communication established
# where the client can send a message to a server and the server log
# the data in the most basic communication
# this is so we may troubleshoot the IOT Test bench communication and
# locate the problem of why its waiting for communication
import multiprocessing
import socket
import re
import sys
import time
import datetime
import sqlite3
# c.execute('''CREATE TABLE testing (Entry, Data, Client Address, Date Recieved)''')

host = ''
port = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# bind socket to specified port
s.bind((host, port))
s.listen(6)
count = 0
print("Waiting for a connection ..")

# decode the data
while True:
    conn = sqlite3.connect(
        '/home/pi/Desktop/iot_test_bench/testfiles/testing.db')
    connection, address = s.accept()
    ip_address, port = str(address[0]), str(address[1])
    try:
        #print('Connection established with', address)
        data = connection.recv(1024)
        datadecode = data.decode('utf-8')
        array = datadecode.split(",")
        appliance, message, mac_address, datetime = str(
            array[0]), str(array[1]), str(array[2]), str(array[3])

        count = count+1
        c = conn.cursor()
        print(data)
        print("Connection Established with: ", ip_address, "\n Through port: ",
              port, "\n", appliance, "\n", message, "\n ", mac_address, "\n", datetime)
        print(' Data '+str(count))
        print("Awaiting new data")
        c.execute("INSERT INTO testing VALUES (?,?,?,?,?)",
                  (datetime, appliance, message, ip_address, mac_address))
        conn.commit()
        conn.close()

    except socket.error:
        print("Connection Failed...")
        conn.close()
