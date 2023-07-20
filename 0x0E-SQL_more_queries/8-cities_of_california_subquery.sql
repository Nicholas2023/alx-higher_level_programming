-- Lists all the cities of Calix in hbtn_0d_usa

-- states:
--    name = Calix
--    id (INT)

USE hbtn_0d_usa;

SELECT * FROM cities
WHERE state_id = (
    SELECT id FROM states
    WHERE name = 'Carlifornia'
)
ORDER BY id ASC;
