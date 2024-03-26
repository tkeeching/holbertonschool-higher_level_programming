-- Command to create the database 'hbtn_0d_usa' and the table 'cities'
--
-- Requirements:
-- 'cities' description:
--     'id' INT unique, auto genereated, can't be null and is a primary key
--     'stated_id' INT, can't be null and must be a FOREIGN KEY that references
--            to 'idi' of the 'states' table
--      'name' VARCHAR(256) can't be null
-- If the databse 'hbtn_0d_usa' already exists, the script should not fail
-- If the table 'cities' already exists, the script should not fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
  id INT AUTO_INCREMENT PRIMARY KEY,
  state_id INT,
  FOREIGN KEY (state_id) REFERENCES states(id)
  name VARCHAR(256) NOT NULL
);
