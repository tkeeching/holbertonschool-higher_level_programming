-- Command to list all the cities in 'hbtn_0d_usa'
--
-- Requirements:
--    Each record should display 'cities.id' - 'cities.name' - 'states.name'
--    Results must be sorted in ascending order by 'cities.id'
--    You are not allowed to use the 'JOIN' keyword

SELECT cities.id, cities.name FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
