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
SELECT city,
SUM(cases_reported) AS Total_Crimes
FROM crime_reports
GROUP BY city
ORDER BY Total_Crimes DESC
LIMIT 10;
"""

df = pd.read_sql(query, conn)

print(df)

plt.figure(figsize=(10,5))
plt.bar(df["city"], df["Total_Crimes"])
plt.title("Top 10 Crime Cities")
plt.xlabel("City")
plt.ylabel("Total Crimes")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

conn.close()