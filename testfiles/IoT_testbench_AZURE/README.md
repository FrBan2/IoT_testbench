DEPA LAB IOT_TESTBENCH
======================
The IoT TestBench is a DEPA Lab project that maintains the communication of multiple devices. Then logs the communication to Microsoft AZURE Sql. Followed by producing d3 visualization for comprehensive data analysis.

Resources
---------------
* Raspberry Pi  
* Microsoft AZURE Account  
* Python  
* D3  

SetUp
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
 3. Create Table 
   * Database >> Query editor >> (Login in with credentials)>> New Query
   ```
   CREATE TABLE CommLogs (Client nvarchar(46), Mac_Addr nvarchar(200), Occurance_Time nvarchar(100));
   ```
 4. Create config.py 
 ```
 DATABASE_CONFIG = {
    'server': '<SERVERNAME>.database.windows.net',
    'database': '<DATABASENAME>',
    'username': '<USERNAME>@<SERVERNAME>.com',
    'password': '<PASSWORD>',
    'tablename': 'dbo.<TABLENAME>'
}
```
 
 5. Create client.py
  ```
  pip install pyodbc
  pip install pandas
  pip install azure
  pip install azure-cli
  ```
  
