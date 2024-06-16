-- Task 1. Creates the MySQL server user user_0d_1.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- create the user if it does not exists
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
-- granting all privileges to the user