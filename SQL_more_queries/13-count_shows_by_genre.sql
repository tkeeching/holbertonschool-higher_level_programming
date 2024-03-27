-- Command to list all genres from 'hbtn_0d_tvshows' and displays the number of shows linked to each
--
-- Requirements:
--    Each record should display <TV Show genre> - <Number of shows linked to this genre>
--    First column must be called 'genre'
--    Second column must be called 'number_of_shows'
--    Don’t display a genre that doesn’t have any shows linked
--    Results must be sorted in descending order by the number of shows linked
--    If a show doesn’t have a genre, display 'NULL'
--    You can use only one 'SELECT' statement

SELECT
    tv_show_genres.name AS genre,
    tv_shows.genre_id,
    @counter := IF(@prev_foreign_key = tv_shows.genre_id, @counter + 1, 1) AS accumulative_count,
    @prev_foreign_key := tv_shows.genre_id
FROM 
    tv_show_genres 
JOIN 
    tv_shows ON tv_show_genres.show_id = tv_shows.id
ORDER BY
    genre, number_of_shows;
