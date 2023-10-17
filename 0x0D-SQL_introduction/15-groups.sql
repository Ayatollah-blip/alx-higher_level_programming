-- A full creation of a new table with values'--
SELECT score, count(*) AS number
FROM second_table
GROUP BY score;
