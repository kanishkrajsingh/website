import mysql.connector
dataBase = mysql.connector.connect(

    host = 'localhost',
    user = 'root',
    passwd ='Root123!'

)

cursorObject = dataBase.cursor()
        
cursorObject.execute("CREATE DATABASE elderco")
print("all done")  
