-- Creates a table: id_not_null

-- id_not_null
--    id (INT): With default value of 1
--    name (VARCHAR)

-- Db name to be passed as an arg
-- If the table exists, the script should not fail

CREATE TABLE IF NOT EXISTS `id_not_null` (
    `id` INT DEFAULT 1,
    `name` VARCHAR(256)
);
