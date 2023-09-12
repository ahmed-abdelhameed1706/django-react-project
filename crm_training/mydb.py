import mysql.connector 

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'K@7wmft999',
)

cursorObject = database.cursor()

cursorObject.execute('CREATE DATABASE crm')

print("It works!")