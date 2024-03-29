-- Creates a database: hbtn_0d_usa and table: states

-- states:
--    id (INT): unique, auto-gen
--    name (VARCHAR): Not NULL

-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Switch to the database
USE hbtn_0d_usa;

-- Create the states table if it doesn't exist
CREATE TABLE IF NOT EXISTS states (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(256) NOT NULL
);
