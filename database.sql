--Create a database and table for smart city crime reports

CREATE DATABASE smart_city_crime;

--use the database
USE smart_city_crime;

-- create a table to store crime reports

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



--check the structure of the table

SHOW TABLES;

DESCRIBE crime_reports;


-- showing all records in the table
use smart_city_crime;

SELECT * FROM crime_reports;

--row count of the table

SELECT COUNT(*) AS Total_Records
FROM crime_reports;


--cities wise total cases reported

SELECT city,
SUM(cases_reported) AS Total_Cases
FROM crime_reports
GROUP BY city
ORDER BY Total_Cases DESC;


--year wise total cases reported

SELECT year,
SUM(cases_reported) AS Total_Cases
FROM crime_reports
GROUP BY year
ORDER BY year;



--crime category wise total cases reported

SELECT crime_category,
COUNT(*) AS Total
FROM crime_reports
GROUP BY crime_category;


-- severity wise total cases reported
SELECT *
FROM crime_reports
WHERE severity='High';


--closed cases in the table

SELECT *
FROM crime_reports
WHERE case_status='Closed';

Use smart_city_crime;

--State wise total cases reported
SELECT
    state,
    COUNT(*) AS total_reports,
    SUM(cases_reported) AS total_cases
FROM crime_reports
GROUP BY state
ORDER BY total_cases DESC;





--terminate the table and delete all records but not stucture of the table
TRUNCATE TABLE crime_reports;

