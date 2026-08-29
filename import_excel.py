import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mdsajid@2373",      
    database="smart_city_crime"
)

cursor = conn.cursor()

df = pd.read_excel("India_Smart_Cities_Crime_Report_2020_2026.xlsx")

query = """
INSERT IGNORE INTO crime_reports
(
report_no,
crime_date,
year,
city,
state,
crime_category,
crime_type,
severity,
cases_reported,
case_status
)
VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""

for _, row in df.iterrows():
    values = (
        row["Crime_ID"],
        row["Date"],
        row["Year"],
        row["City"],
        row["State"],
        row["Crime_Category"],
        row["Crime_Type"],
        row["Severity"],
        row["Cases_Reported"],
        row["Case_Status"]
    )

    cursor.execute(query, values)

conn.commit()

print("Data Imported Successfully!")

cursor.close()
conn.close()