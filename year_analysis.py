import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mdsajid@2373",   
    database="smart_city_crime"
)

query = """
SELECT year,
SUM(cases_reported) AS Total_Crimes
FROM crime_reports
GROUP BY year
ORDER BY year;
"""

df = pd.read_sql(query, conn)

print(df)

plt.figure(figsize=(8,5))
plt.plot(df["year"], df["Total_Crimes"], marker="o")
plt.title("Year-wise Crime Trend")
plt.xlabel("Year")
plt.ylabel("Total Crimes")
plt.grid(True)
plt.show()

conn.close()