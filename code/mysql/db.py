import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='toor',
    database='prueba'
)

cursor = mydb.cursor()

# Insert
# sql = 'Insert into Usuario (email, username, edad) values (%s,%s,%s)'
# values = ('elcorreo@op.com', 'usernom', 27)

# Update
# sql = 'Update Usuario set email = %s where id = %s'
# values = ('elcorreo@opa.co.es', 4)

# Delete
sql = 'Delete from Usuario where id = %s'
values = (4, )

cursor.execute(sql, values)
mydb.commit()

# Select
cursor.execute('Select * from Usuario')
# cursor.execute('Select * from Usuario limit 2') #limita la cantidad de elementos recuperados ;)

for row in cursor.fetchall():
    print(row)
