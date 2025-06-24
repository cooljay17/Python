# Importing Sqlite3 Module
import sqlite3

try:
    
    # Making a connection between sqlite3 
    # database and Python Program
    sqliteConnection = sqlite3.connect('database.db')
    
    # If sqlite3 makes a connection with python
    # program then it will print "Connected to SQLite"
    # Otherwise it will show errors
    print("Connected to SQLite")

    # Getting all tables from sqlite_master
    # Display columns
    cursor = sqliteConnection.cursor()
            
    # Display data
    print('\nData in EMPLOYEE table:')
    data=cursor.execute('''SELECT * FROM book''')
    for row in data:
        print(row)

except sqlite3.Error as error:
    print("Failed to execute the above query", error)
    
finally:
  
    # Inside Finally Block, If connection is
    # open, we need to close it
    if sqliteConnection:
        
        # using close() method, we will close 
        # the connection
        sqliteConnection.close()
        
        # After closing connection object, we 
        # will print "the sqlite connection is 
        # closed"
        print("the sqlite connection is closed")