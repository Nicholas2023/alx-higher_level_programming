-- Creates the MYSQL server user_0d_1

-- user_0d_1 should have all privileges on mysql server
-- user_0d_1 password should bet set to user_0d_1_pwd
-- if user_0d_1 already exists, the script should not fail

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED WITH mysql_native_password BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
