-- Command to list all comedy shows in 'hbtn_0d_tvshows'
--
-- Requirements:
--    The 'tv_genres' table contains only one record where 'name' = 'Comedy' (but the id can be different)
--    Each record should display tv_shows.title
--    Results must be sorted in ascending order by show title
--    You can use only one 'SELECT' statement

SELECT
    tv_shows.title
FROM
    tv_shows
JOIN
    tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN
    tv_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE
    tv_genres.name = 'Comedy'
ORDER BY
    tv_shows.title;
