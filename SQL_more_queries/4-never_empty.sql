-- Command to create the table 'id_not_null'
--
-- Requirements:
-- 'id_not_null' description:
--     'id' INT with default value 1
--     'name' VARCHAR(256)
-- If the table 'force_name' already exists, the script should not fail

CREATE TABLE IF NOT EXISTS id_not_null {
  id INT AUTO_INCREMENT PRIMARY KEY DEFAULT 1,
  name VARCHAR(256)
}
