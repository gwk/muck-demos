.open data.sqlite3
.mode csv
.headers on

SELECT country, MAX(year)
FROM expectancies
WHERE var == 'EVIETOTA'
AND unit == 'EVIDUREV'
GROUP BY country;
