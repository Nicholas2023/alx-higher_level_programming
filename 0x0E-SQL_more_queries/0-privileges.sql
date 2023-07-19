-- Check privileges for user_0d_1
SELECT 
  USER, 
  HOST, 
  MAX_USER_CONNECTIONS,
  MAX_QUERIES_PER_HOUR,
  MAX_UPDATES_PER_HOUR,
  MAX_CONNECTIONS_PER_HOUR
FROM 
  mysql.user
WHERE 
  USER = 'user_0d_1' AND
  HOST = 'localhost';

-- Check privileges for user_0d_2
SELECT 
  USER, 
  HOST, 
  MAX_USER_CONNECTIONS,
  MAX_QUERIES_PER_HOUR,
  MAX_UPDATES_PER_HOUR,
  MAX_CONNECTIONS_PER_HOUR
FROM 
  mysql.user
WHERE 
  USER = 'user_0d_2' AND
  HOST = 'localhost';
