-- Creates table: force_name on mysql server

-- If force_name already exist; script should not fail
-- force_name:
--    id (INT)
--    name (VARCHAR) : NOT NULL

-- The db name will be passed as an arg of mysql cmd

CREATE TABLE IF NOT EXISTS `force_name` (
    `id` INT,
    `name` VARCHAR(256) NOT NULL,
);
