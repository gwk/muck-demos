.open 'data.sqlite3'
.mode csv
.headers on
SELECT DISTINCT HP, Provider FROM expenditures;
