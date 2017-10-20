.open data.sqlite3
.mode csv
.headers on

SELECT
  privateExpend.country AS Country,
  printf("%7.2f", privateExpend.value) AS 'Private Cost',
  printf("%7.2f", totalExpend.value) AS 'Total Cost',
  latestExpectancies.value as 'Life Expectancy',
  latestExpectancies.year as 'LE Year'

FROM expenditures AS privateExpend
LEFT JOIN expenditures AS totalExpend ON privateExpend.country == totalExpend.country
LEFT JOIN
  (SELECT value, country, MAX(year) as year
  FROM expectancies
  WHERE var == 'EVIETOTA'
  AND unit == 'EVIDUREV'
  GROUP BY country) AS latestExpectancies
 ON privateExpend.country == latestExpectancies.country

WHERE
    privateExpend.HF == 'HF2HF3'
AND privateExpend.HC == 'HCTOT'
AND privateExpend.HP == 'HPTOT'
AND privateExpend.measure == 'VRPPPR'
AND privateExpend.year == 2016

AND totalExpend.HF == 'HFTOT'
AND totalExpend.HC == 'HCTOT'
AND totalExpend.HP == 'HPTOT'
AND totalExpend.measure == 'VRPPPR'
AND totalExpend.year == 2016

ORDER BY privateExpend.value DESC;
