# Smart City Crime Management & Analysis

## 📌 Project Overview

This project is a **Smart City Crime Management and Analysis System**
for studying crime reports across Indian cities for the period
**2020--2026**.

The project combines:

-   **CSV/Excel** for the source dataset
-   **MySQL** for storing and querying crime records
-   **Python** for database connectivity, data import, analysis, and
    visualization
-   **Matplotlib** for charts

The supplied dataset contains **700 crime records**, **10 columns**,
**50 cities**, and **23 states**, covering the years **2020--2026**.

> **Note:** This dataset is suitable for an academic/project
> demonstration. It should not be treated as official government crime
> statistics.

------------------------------------------------------------------------

## 📂 Project Files

  -------------------------------------------------------------------------------------
  File                                              Purpose
  ------------------------------------------------- -----------------------------------
  `database.sql`                                    Creates the MySQL database/table
                                                    and contains SQL analysis queries

  `connection.py`                                   Tests the Python-to-MySQL
                                                    connection

  `import_excel.py`                                 Imports the Excel dataset into
                                                    MySQL

  `display_record.py`                               Retrieves and displays all records
                                                    from MySQL

  `state_analysis.py`                               Performs state-wise analysis and
                                                    creates a bar chart

  `year_analysis.py`                                Performs year-wise analysis and
                                                    creates a line chart

  `city_analysis.py`                                Finds the top 10 cities by reported
                                                    cases and creates a bar chart

  `category_analysis.py`                            Shows crime-category distribution
                                                    using a pie chart

  `India_Smart_Cities_Crime_Report_2020_2026.csv`   Source crime dataset
  -------------------------------------------------------------------------------------

### Python script mapping

The Python files supplied with this project perform the following tasks:

-   **Connection test:** connects to `smart_city_crime` and prints
    `Connected Successfully`.
-   **Data import:** reads the Excel file and inserts records into
    `crime_reports`.
-   **Display records:** executes `SELECT * FROM crime_reports` and
    prints the data.
-   **State analysis:** groups records by state and calculates total
    reports, total cases, and average cases.
-   **Year analysis:** groups cases by year and plots the yearly trend.
-   **City analysis:** finds the top 10 cities by total reported cases.
-   **Category analysis:** groups reports by crime category and displays
    the distribution.

------------------------------------------------------------------------

## 🗃️ Dataset Information

### Dataset size

-   **Records:** 700
-   **Columns:** 10
-   **Years:** 2020, 2021, 2022, 2023, 2024, 2025, 2026
-   **Cities:** 50
-   **States:** 23
-   **Total reported cases:** 179,418

### Crime categories

-   Cyber
-   Property
-   Traffic
-   Violent
-   Women

### Crime types

-   Assault
-   Burglary
-   Drunk Driving
-   Harassment
-   Hit and Run
-   Phishing
-   Robbery
-   Stalking
-   Theft
-   UPI Fraud

### Severity levels

-   High
-   Medium
-   Low

### Case statuses

-   Open
-   Closed
-   Under Investigation
-   Chargesheet Filed

### Dataset columns

  Column             Description
  ------------------ ---------------------------------------------------
  `Crime_ID`         Unique crime/report identifier in the source file
  `Date`             Date of the crime report
  `Year`             Year of the report
  `City`             Indian city associated with the report
  `State`            State/region associated with the city
  `Crime_Category`   Broad crime category
  `Crime_Type`       Specific crime type
  `Severity`         High, Medium, or Low
  `Cases_Reported`   Number of cases reported
  `Case_Status`      Current status of the report

------------------------------------------------------------------------

## 🛠️ Technologies Used

-   Python 3
-   MySQL
-   Pandas
-   MySQL Connector/Python
-   Matplotlib
-   Excel/CSV
-   VS Code (recommended)

------------------------------------------------------------------------

## 📦 Python Requirements

Install the required packages from the VS Code terminal:

``` bash
pip install pandas mysql-connector-python matplotlib openpyxl
```

`openpyxl` is required when using the Excel import script.

------------------------------------------------------------------------

# 🚀 Project Setup and Execution

Follow these steps in order.

## Step 1 --- Start MySQL

Make sure your MySQL Server is running.

You can use MySQL Workbench, VS Code with a MySQL extension, or the
MySQL command line.

------------------------------------------------------------------------

## Step 2 --- Create the database and table

Open `database.sql` in your MySQL client and run the database/table
creation section:

``` sql
CREATE DATABASE smart_city_crime;

USE smart_city_crime;

CREATE TABLE crime_reports (
    report_no VARCHAR(20) PRIMARY KEY,
    crime_date DATE,
    year INT,
    city VARCHAR(50),
    state VARCHAR(50),
    crime_category VARCHAR(50),
    crime_type VARCHAR(50),
    severity VARCHAR(20),
    cases_reported INT,
    case_status VARCHAR(50)
);
```

Verify the table:

``` sql
SHOW TABLES;

DESCRIBE crime_reports;
```

------------------------------------------------------------------------

## Step 3 --- Configure the Python MySQL connection

The Python files use:

``` python
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_MYSQL_PASSWORD",
    database="smart_city_crime"
)
```

Replace `YOUR_MYSQL_PASSWORD` with your local MySQL password.

### Security recommendation

Do **not** commit your real MySQL password to GitHub.

For a public repository, use an environment variable or a separate
configuration file that is included in `.gitignore`.

------------------------------------------------------------------------

## Step 4 --- Test the MySQL connection

Run:

``` bash
python connection.py
```

Expected output:

``` text
Connected Successfully
```

If you receive an authentication error, check your MySQL
username/password.

If you receive:

``` text
Unknown database 'smart_city_crime'
```

run the database creation SQL first.

------------------------------------------------------------------------

## Step 5 --- Import the dataset

The supplied import script currently uses:

``` python
df = pd.read_excel("India_Smart_Cities_Crime_Report_2020_2026.xlsx")
```

So if you have the Excel version of the dataset, keep the Excel file in
the same project folder and run:

``` bash
python import_excel.py
```

Expected output:

``` text
Data Imported Successfully!
```

### If you only have the CSV file

Change:

``` python
pd.read_excel(...)
```

to:

``` python
pd.read_csv("India_Smart_Cities_Crime_Report_2020_2026.csv")
```

Then run the import script again.

The supplied import code uses `INSERT IGNORE`, which helps avoid errors
when a `report_no` already exists in the table.

------------------------------------------------------------------------

## Step 6 --- Verify the imported records

Run in MySQL:

``` sql
USE smart_city_crime;

SELECT * FROM crime_reports;

SELECT COUNT(*) AS Total_Records
FROM crime_reports;
```

The supplied dataset contains 700 source records.

You can also run:

``` bash
python display_record.py
```

The script retrieves the records with:

``` sql
SELECT * FROM crime_reports;
```

------------------------------------------------------------------------

# 📊 SQL Analysis

The `database.sql` file contains several analysis queries.

### Total records

``` sql
SELECT COUNT(*) AS Total_Records
FROM crime_reports;
```

### City-wise total cases

``` sql
SELECT city,
       SUM(cases_reported) AS Total_Cases
FROM crime_reports
GROUP BY city
ORDER BY Total_Cases DESC;
```

### Year-wise total cases

``` sql
SELECT year,
       SUM(cases_reported) AS Total_Cases
FROM crime_reports
GROUP BY year
ORDER BY year;
```

### Crime-category distribution

``` sql
SELECT crime_category,
       COUNT(*) AS Total
FROM crime_reports
GROUP BY crime_category;
```

### High-severity reports

``` sql
SELECT *
FROM crime_reports
WHERE severity = 'High';
```

### Closed cases

``` sql
SELECT *
FROM crime_reports
WHERE case_status = 'Closed';
```

### State-wise analysis

``` sql
SELECT
    state,
    COUNT(*) AS total_reports,
    SUM(cases_reported) AS total_cases
FROM crime_reports
GROUP BY state
ORDER BY total_cases DESC;
```

------------------------------------------------------------------------

# 📈 Python Analysis and Visualizations

## 1. State-wise Crime Analysis

`state_analysis.py` calculates:

-   Total reports by state
-   Total cases by state
-   Average cases per report

It then creates a **State-wise Crime Analysis** bar chart.

Run:

``` bash
python state_analysis.py
```

------------------------------------------------------------------------

## 2. Year-wise Crime Trend

`year_analysis.py` calculates total reported cases for each year and
creates a line chart.

Run:

``` bash
python year_analysis.py
```

The chart shows the trend from **2020 to 2026**.

------------------------------------------------------------------------

## 3. Top 10 Crime Cities

`city_analysis.py` finds the 10 cities with the highest total reported
cases.

Run:

``` bash
python city_analysis.py
```

Output:

-   Top 10 cities
-   Total cases for each city
-   Bar chart

------------------------------------------------------------------------

## 4. Crime Category Distribution

`category_analysis.py` groups reports by `crime_category` and creates a
pie chart.

Run:

``` bash
python category_analysis.py
```

The chart displays the distribution of categories such as Cyber,
Property, Traffic, Violent, and Women.

------------------------------------------------------------------------

# 🔄 Complete Execution Flow

Use this order when running the project:

``` text
1. Start MySQL
       ↓
2. Run database.sql
       ↓
3. Create smart_city_crime database
       ↓
4. Create crime_reports table
       ↓
5. Run connection.py
       ↓
6. Run import_excel.py
       ↓
7. Verify records in MySQL
       ↓
8. Run display_record.py
       ↓
9. Run state_analysis.py
       ↓
10. Run year_analysis.py
       ↓
11. Run city_analysis.py
       ↓
12. Run category_analysis.py
```

------------------------------------------------------------------------

# 🎯 Project Objectives

The main objectives of this project are:

1.  Store structured crime reports in MySQL.
2.  Import crime data from Excel/CSV using Python.
3.  Retrieve and display records from MySQL.
4.  Analyze crime patterns by state, city, year, and category.
5.  Analyze crime severity and case status.
6.  Create visual representations of crime trends.
7.  Demonstrate integration between Python and MySQL.

------------------------------------------------------------------------

# 📌 Key Analysis Areas

The project supports:

-   **State-wise crime analysis**
-   **City-wise crime analysis**
-   **Top 10 cities by reported cases**
-   **Year-wise crime trends**
-   **Crime-category distribution**
-   **High-severity crime identification**
-   **Closed-case identification**
-   **Case-status analysis**
-   **Average cases per report**

------------------------------------------------------------------------

# ⚠️ Important Notes

### 1. Avoid running `TRUNCATE` accidentally

The supplied SQL file contains:

``` sql
TRUNCATE TABLE crime_reports;
```

This removes **all records** from the table while keeping the table
structure.

Run it only if you intentionally want to reset the table before
importing the data again.

### 2. Duplicate records

The Python import script uses:

``` sql
INSERT IGNORE
```

Therefore, a record with an already-existing `report_no` will be ignored
instead of causing a duplicate-primary-key error.

### 3. Database name

All supplied Python scripts are configured for:

``` text
smart_city_crime
```

Make sure the database name is consistent across MySQL and Python.

### 4. Password security

Never upload your actual MySQL password to a public GitHub repository.

------------------------------------------------------------------------

# 🧪 Example Project Outputs

After completing the setup, the project can produce:

-   MySQL crime database
-   Imported crime records
-   State-wise crime table
-   Year-wise crime trend
-   Top 10 city chart
-   Crime category pie chart
-   Severity-based analysis
-   Case-status analysis

------------------------------------------------------------------------

# 📁 Suggested GitHub Repository Structure

``` text
smart-city-crime/
│
├── README.md
├── database.sql
│
├── connection.py
├── import_excel.py
├── display_record.py
├── state_analysis.py
├── year_analysis.py
├── city_analysis.py
├── category_analysis.py
│
├── India_Smart_Cities_Crime_Report_2020_2026.csv
│
└── .gitignore
```

Recommended `.gitignore` entries:

``` text
__pycache__/
*.pyc
.env
.vscode/
```

------------------------------------------------------------------------

# 👨‍💻 Project Summary

**Smart City Crime Management & Analysis** is an academic data-analysis
project that demonstrates how crime-report data can be stored in MySQL,
accessed through Python, analyzed using SQL/Pandas, and visualized using
Matplotlib.

The project covers **700 records across 50 Indian cities and 23 states
for 2020--2026** and provides multiple analytical views including
state-wise, city-wise, year-wise, and category-wise crime analysis.

------------------------------------------------------------------------

## 📜 License

This project is intended for educational and academic use.

The included dataset is a project dataset and should not be interpreted
as official government crime statistics.
