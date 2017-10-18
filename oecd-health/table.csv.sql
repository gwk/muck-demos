.open data.sqlite3
.mode csv
.headers on

SELECT
  privateExpend.country AS Country,
  printf("%7.2f", privateExpend.value) AS 'Private Cost',
  printf("%7.2f", totalExpend.value) AS 'Total Cost',
  expectancies.value as 'Life Expectancy'

FROM expenditures AS privateExpend
LEFT JOIN expenditures AS totalExpend ON privateExpend.country == totalExpend.country
LEFT JOIN expectancies ON privateExpend.country == expectancies.country

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

AND expectancies.year == 2015 -- The 2016 data is incomplete, so we use the prior year instead.
AND expectancies.var == 'EVIETOTA'
AND expectancies.unit == 'EVIDUREV'

ORDER BY privateExpend.value DESC;
