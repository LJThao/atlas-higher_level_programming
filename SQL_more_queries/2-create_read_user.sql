-- Task 2. Creates the database hbtn_0d_2 and the user user_0d_2.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- create database if the database doesn't exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- create a new user with a password if the user doesn't exist
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
-- grant the user permission to select data from all tables from the database