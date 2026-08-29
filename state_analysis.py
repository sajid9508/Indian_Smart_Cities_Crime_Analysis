import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

# -----------------------------
# Connect to MySQL
# -----------------------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mdsajid@2373",
    database="smart_city_crime"
)

# -----------------------------
# State-wise Analysis
# -----------------------------
query = """
SELECT
    state,
    COUNT(*) AS total_reports,
    SUM(cases_reported) AS total_cases,
    AVG(cases_reported) AS average_cases
FROM crime_reports
GROUP BY state
ORDER BY total_cases DESC;
"""

df = pd.read_sql(query, conn)

print("\nSTATE-WISE CRIME ANALYSIS")
print(df.to_string(index=False))

# -----------------------------
# Bar Chart
# -----------------------------
plt.figure(figsize=(12, 6))

plt.bar(df["state"], df["total_cases"])

plt.title("State-wise Crime Analysis")
plt.xlabel("State")
plt.ylabel("Total Cases")

plt.xticks(rotation=60)
plt.tight_layout()

plt.show()

# -----------------------------
# Close Connection
# -----------------------------
conn.close()