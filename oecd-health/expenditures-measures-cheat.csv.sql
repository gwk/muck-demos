.open 'data.sqlite3'
.mode csv
.headers on
SELECT DISTINCT MEASURE, Measure_1, Country, Value, Year, Reference_Period AS 'Base Year'
FROM expenditures
WHERE HF == 'HF2HF3'
AND HC == 'HCTOT'
AND HP == 'HPTOT'
AND Unit_Code == 'USD'
AND PowerCode == 'Units'
AND Year = 2016
AND (
     (Location == 'USA' AND Value BETWEEN 4100 AND 5100) -- article: 4,570.50
  OR (Location == 'CHE' AND Value BETWEEN 2600 AND 3600) -- article: 3,097.20
  OR (Location == 'AUS' AND Value BETWEEN 1300 AND 2300) -- article: 1,783.90
  OR (Location == 'CAN' AND Value BETWEEN 1000 AND 2000) -- article: 1,531.70
)
ORDER BY Value DESC;
