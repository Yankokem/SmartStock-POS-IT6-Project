import mysql.connector
print("Attempting to connect...")
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='smarstock_inventory'
)
print("Connected!")
conn.close()