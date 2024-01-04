#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa
takes 3 arguments: mysql username, mysql password and database name
"""


import MySQLdb
from sys import argv

if __name__ == '__main__':
    """connect to database"""
    db_connection = MySQLdb.connect(
            host="localhost", port=3306, user=argv[1],
            passwd=argv[2], db=argv[3])

    cursor = db_connection.cursor()
    msg = """SELECT * FROM states WHERE name LIKE BINARY '{:s}'
    ORDER BY id ASC""".format(argv[4])
    cursor.execute(msg)
    for rows in cursor.fetchall():
        print(rows)
    db_connection.close()
