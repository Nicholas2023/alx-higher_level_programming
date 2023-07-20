-- Lists all the cities of Calix in hbtn_0d_usa

-- states:
--    name = Calix
--    id (INT)

SELECT `id`, `name`
  FROM `cities`
 WHERE `state_id` IN
       (SELECT `id`
	  FROM `states`
	 WHERE `name` = "California")
 ORDER BY `id`;
