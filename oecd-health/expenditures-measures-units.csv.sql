.open 'data.sqlite3'
.mode csv
.headers on
SELECT DISTINCT MEASURE, Measure_1, Unit_Code, Unit, PowerCode, Reference_Period
FROM expenditures
ORDER BY MEASURE;
