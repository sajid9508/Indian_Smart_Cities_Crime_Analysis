import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mdsajid@2373",   
    database="smart_city_crime"
)

query = "SELECT * FROM crime_reports"

df = pd.read_sql(query, conn)

print(df)

conn.close()