-- Creates the table id_not_null on your MySQL server.
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
-- id INT DEFAULT 1 = unique id for a record and if no value then defaults to 1.
-- name VARCHAR(256) = the name linked to the ID and can be NULL