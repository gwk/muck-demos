.open 'data.sqlite3'
.mode csv
.headers on
SELECT DISTINCT VAR, Variable FROM expectancies;
