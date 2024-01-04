#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
takes 3 arguments: mysql username, mysql password and database name
"""


from sys import argv
import MySQLdb

if __name__ == '__main__':
    """connect to database"""
    db_connection = MySQLdb.connect(
            host="localhost", port=3306, user=argv[1],
            passwd=argv[2], db=argv[3])

    cursor = db_connection.cursor()
    qry = "SELECT cities.id, cities.name, states.name \
          FROM cities, states WHERE cities.state_id = states.id \
          ORDER BY cities.id ASC"
    cursor.execute(qry)
    for rows in cursor.fetchall():
        print(rows)
    db_connection.close()
