.open 'data.sqlite3'
.mode csv
.headers on
SELECT DISTINCT HF, Financing_scheme FROM expenditures;
