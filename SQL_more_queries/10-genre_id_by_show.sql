-- Command to list all shows contained in 'hbtn_0d_tvshows' that have at least one genre linked
--
-- Requirements:
--    Each record should display 'tv_shows.title' - 'tv_shows_genres.genre_id'
--    Results must be sorted in ascending order by 'tc_shows.title' and 'tv_show_genres.genre_id'
--    You can use only one 'SELECT' keyword

SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_show_genres
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
