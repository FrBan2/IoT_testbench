import socket
import re
import os
import time
from datetime import datetime
from uuid import getnode as get_mac
import random
import pyodbc
import config
import traceback
import pandas as pd


TABLENAME = config.DATABASE_CONFIG['tablename']
DRIVER= '{ODBC Driver 17 for SQL Server}'
CONNECTION_STRING = 'DRIVER=' + DRIVER + \
                    ';SERVER=' + config.DATABASE_CONFIG['server'] + \
                    ';PORT=1433' + \
                    ';DATABASE=' + config.DATABASE_CONFIG['database'] + \
                    ';UID=' + config.DATABASE_CONFIG['username'] + \
                    ';PWD=' + config.DATABASE_CONFIG['password'] 
SQL_CONN = pyodbc.connect(CONNECTION_STRING)
C = SQL_CONN.cursor()
CLIENT = 'Thermostat'
MAC_ADDR = (':'.join(re.findall('..', '%012x' % get_mac())))

def write2db():

     h = ["07", "07", "08", "08", "08", "08", "15", "15",
     "16", "16", "17", "17", "17", "17", "18", "18"]

     for h in h:

          min = str(random.randint(0, 60)).zfill(2)
          sec = str(random.randint(0, 60)).zfill(2)
          timestamp = (datetime.utcnow().strftime('%Y-%m-%d'))+'-'+(h)+'-'+(min)+'-'+(sec)
          message = ('Camera, '+(MAC_ADDR).upper()+', ' +timestamp)
          print (message)
          # array = message.split(",")
          # appliance, mac_address, timestamp = array[0], array[1], array[2]
          C.execute("INSERT INTO TestbenchComLogs Values (?,?,?)",
                         (CLIENT, MAC_ADDR.upper(), timestamp))

          C.commit()
          time.sleep(5)
     C.close()
        
if __name__ == "__main__":
    write2db()
