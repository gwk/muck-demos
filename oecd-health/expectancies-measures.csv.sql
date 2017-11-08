.open 'data.sqlite3'
.mode csv
.headers on
SELECT DISTINCT UNIT, Measure FROM expectancies;
