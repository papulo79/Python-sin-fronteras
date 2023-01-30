import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='toor',
    database='prueba'
)

cursor = mydb.cursor()

cursor.execute('Select * from Usuario')

for row in cursor.fetchall():
    print(row)
