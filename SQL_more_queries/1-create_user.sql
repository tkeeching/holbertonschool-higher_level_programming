-- Command to create MySQL server user 'user_0d_1'
--
-- Requirements:
-- 'user_0d_1' should have all privileges
-- The 'user_0d_1' password should be set to 'user_0d_1_pwd'
-- Id the user 'user_0d_1' already exists, the script should not fail

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL ON *.* TO 'user_0d_1'@'localhost';
