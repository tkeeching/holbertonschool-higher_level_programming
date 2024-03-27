-- Command to list all shows and all genres linked to that show in 'hbtn_0d_tvshows'
--
-- Requirements:
--    If a show doesn’t have a genre, display 'NULL' in the genre column
--    Each record should display 'tv_shows.title' - 'tv_genres.name'
--    Results must be sorted in ascending order by show title and genre name
--    You can use only one 'SELECT' statement

SELECT
    tv_shows.title, IFNULL(tv_genres.name, 'NULL')
FROM
    tv_shows
LEFT JOIN
    tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN
    tv_genres ON tv_genres.id = tv_show_genres.genre_id
ORDER BY
    tv_shows.title, tv_genres.name;
