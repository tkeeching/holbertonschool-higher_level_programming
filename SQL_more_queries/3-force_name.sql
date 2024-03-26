-- Command to create the table 'force_name'
--
-- Requirements:
-- 'force_name' description:
--     'id' INT
--     'name' VARCHAR(256) can’t be null
-- If the table 'force_name' already exists, the script should not fail

CREATE TABLE force_name {
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(256) NOT NULL
}
