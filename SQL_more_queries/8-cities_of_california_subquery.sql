-- Command to list all the cities of California that can be found in 'hbtn_0d_usa'
--
-- Requirements:
--    'states' table contains only one record where 'name' = 'California' (but the 'id' can be different)
--    Results must be sorted in ascending order by 'cities.id'
--    You are not allowed to use the 'JOIN' keyword

SELECT * FROM cities WHERE states.name = 'California' ORDER BY cities.id ASC ;
