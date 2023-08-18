#!/usr/bin/python3
"""
Display all values in the states table of hbtn_0e_0_usa
where name matches the argument
"""

import sys
import MySQLdb

if __name__ == "__main__":
    """
    Get MySQL credentials and state name from cmd line args
    """
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    """
    Connect to MySQL server
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    """
    Create a cursor object to interact with the database
    """
    cursor = db.cursor()

    """
    Create and execute the SQL query with user input
    """
    query = "SELECT * FROM states WHERE name = %s ORDER BY id"
    cursor.execute(query, (state_name,))

    """
    Fetch all the results
    """
    results = cursor.fetchall()

    """
    Display the results
    """
    for row in results:
        print(row)

    """
    Close the cursor and database connection
    """
    cursor.close()
    db.close()