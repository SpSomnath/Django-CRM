# Install Mysql on computer 
# https://dev.mysql.com/downloads/installer/
# pip install mysql 
# pip install mysql-connector
# pip install mysql-connector-python 

import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Respon@100'
    
)

# prepare a cursor object 
cursorObject = database.cursor()

# create a database 
cursorObject.execute("CREATE DATABASE elderco")

print('all done!')