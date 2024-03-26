-- Command to create the database 'hbtn_0d_usa' and the table 'states'
--
-- Requirements:
-- 'states' description:
--     'id' INT unique, auto genereated, can't be null and is a primary key
--     'name' VARCHAR(256) can't be null
-- If the databse 'hbtn_0d_usa' already exists, the script should not fail
-- If the table 'states' already exists, the script should not fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(256) NOT NULL
);
