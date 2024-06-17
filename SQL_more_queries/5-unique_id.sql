-- Creates the table unique_id on your MySQL server.
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
-- id INT DEFAULT 1 UNIQUE = defines the id column as an int with a default value of 1.
-- name VARCHAR(256) = define the name column as a variable character str that can store up to 256 chars.