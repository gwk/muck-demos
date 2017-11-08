.open 'data.sqlite3'
.mode csv
.headers on
SELECT DISTINCT MEASURE, Measure_1, Reference_Period AS 'Base Year'
FROM expenditures
WHERE Unit_Code == 'USD'
AND PowerCode == 'Units'
ORDER BY MEASURE;
