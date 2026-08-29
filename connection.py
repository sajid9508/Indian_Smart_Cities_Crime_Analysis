import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mdsajid@2373",
    database="smart_city_crime"
)

print("Connected Successfully")

conn.close()