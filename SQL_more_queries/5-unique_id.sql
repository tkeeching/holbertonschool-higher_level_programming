-- Command to create the table 'unique_id'
--
-- Requirements:
-- 'force_name' description:
--     'id' INT with default value 1 and must be unique
--     'name' VARCHAR(256)
-- If the table 'unique_id' already exists, the script should not fail

CREATE TABLE IF NOT EXISTS unique_id (
  id INT PRIMARY KEY,
  name VARCHAR(256)
);
