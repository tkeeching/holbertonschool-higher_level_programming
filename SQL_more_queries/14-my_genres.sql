-- Command to list all genres of the show 'Dexter'
--
-- Requirements:
--    The 'tv_shows' table contains only one record where 'title' = 'Dexter' (but the id can be different)
--    Each record should display tv_genres.name
--    Results must be sorted in ascending order by genre name
--    If a show doesn’t have a genre, display 'NULL'
--    You can use only one 'SELECT' statement

SELECT
    tv_genres.name
FROM
    tv_shows
WHERE
    tv_shows.title = 'Dexter'
RIGHT JOIN
    tv_show_genres ON tv_shows.id = tv_show_genres.show_id
RIGHT JOIN
    tv_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY
    tv_genres.name
ORDER BY
    tv_genres.name;

-- SELECT
--     tv_genres.name
-- FROM
--     tv_genres
-- RIGHT JOIN
--     tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
-- RIGHT JOIN
--     tv_shows ON tv_shows.title = 'Dexter'
-- GROUP BY
--     tv_genres.name
-- ORDER BY
--     tv_genres.name;
