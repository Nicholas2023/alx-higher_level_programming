-- Creates table: unique_id

-- unique_id:
--    id (INT): Default 1
--    name (VARCHAR)

-- Db name will be passed as an arg
-- if table unque_id exists, script should not fail

CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
