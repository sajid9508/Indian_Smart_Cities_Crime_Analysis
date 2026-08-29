import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mdsajid@2373",   # Apna MySQL password
    database="smart_city_crime"
)

query = """
SELECT crime_category,
COUNT(*) AS Total
FROM crime_reports
GROUP BY crime_category;
"""

df = pd.read_sql(query, conn)

plt.figure(figsize=(7,7))
plt.pie(df["Total"], labels=df["crime_category"], autopct="%1.1f%%")
plt.title("Crime Category Distribution")
plt.show()

conn.close()