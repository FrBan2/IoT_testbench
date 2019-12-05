DEPA LAB IOT_TESTBENCH
======================
The IoT TestBench is a DEPA Lab project that maintains the communication of multiple devices. Then logs the communication to Microsoft AZURE Sql. Followed by producing d3 visualization for comprehensive data analysis.

Resources
---------------
* Raspberry Pi  
* Microsoft AZURE Account  
* Python  
* D3  

SetUp AZURE
----------------------
1. Create an AZURE account
   * https://portal.azure.com  
2. Create an SQL DATABASE
   * https://portal.azure.com/#home
   * SQL Databases
     * Create New
   * Subscription: For Students or Free Trial
     * Resource Group = Create new
   * Database Details:
     * Database Name = Choose a name
     * Server = Create new
       * Create a server Name Admin login credentials and choose location.
   * Review + Create
 3. Allowing access
      * Home>>Server>>Firewalls and virtual Networks
      * Insert Ip Address that you want to allow access 
      
 4. Create Table 
   * Database >> Query editor >> (Login in with credentials)>> New Query
   ```
   CREATE TABLE CommLogs (Client nvarchar(46), Mac_Addr nvarchar(200), Occurance_Time nvarchar(100));
   ```
 5. Create config.py 
 ```
 DATABASE_CONFIG = {
    'server': '<SERVERNAME>.database.windows.net',
    'database': '<DATABASENAME>',
    'username': '<USERNAME>@<SERVERNAME>.com',
    'password': '<PASSWORD>',
    'tablename': 'dbo.<TABLENAME>'
}
```
 
 6. Install dependencies
  ```
  sudo apt-get install python-pyodbc
  sudo apt-get install python-pandas 
  ```
  Install ODBC Driver
  Download driver from https://www.microsoft.com/en-us/download/confirmation.aspx?id=48742
  ```
  
  ```
 6. create client.py
 
 
 Visualization
 ----------------
 1. Install node.js on Raspbian
   ```
   curl -sL https://deb.nodesource.com/setup_10.x | sudo bash -
   sudo apt install nodejs
   ```
  * To verify the installation, run the following command which will print the Node.js version:
  ```
  node --version
  ```
  ```
  Output:
  v10.160.0
  ```
  * Development Tools install
  ```
  sudo apt install build-essential
  ```
2. Install d3 
   ```
   npm install d3
   ```
 3. Open Browser to view file:///PATH/index.html
 
 
