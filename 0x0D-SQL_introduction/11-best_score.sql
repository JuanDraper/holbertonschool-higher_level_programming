-- script that retrieves the bests scores and lists them
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
