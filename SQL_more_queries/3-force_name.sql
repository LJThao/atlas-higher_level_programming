-- Creates the table force_name on your MySQL server.
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
-- id INT = unique identifier for each record.
-- name VARCHAR(256) NOT NULL = force name that is provided and cannot have a missing value.