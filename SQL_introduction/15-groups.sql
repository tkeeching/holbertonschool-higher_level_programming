-- Command to list the number of records with the same
-- score in the table 'second_table'
--
-- Requirements:
-- The result should display:
--   the score
--   the number of records for this score with the label number
-- The list should be sorted by the number of records (descending)

SELECT score COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
