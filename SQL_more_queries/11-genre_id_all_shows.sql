-- Command to list all shows contained in 'hbtn_0d_tvshows' that have at least one genre linked
--
-- Requirements:
--    Each record should display 'tv_shows.title' - 'tv_shows_genres.genre_id'
--    Results must be sorted in ascending order by 'tv_shows.title' and 'tv_show_genres.genre_id'
--    If a show doesn’t have a genre, display 'NULL'
--    You can use only one 'SELECT' statement

SELECT tv_shows.title, IFNULL(tv_show_genres.genre_id, 'NULL') AS genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
