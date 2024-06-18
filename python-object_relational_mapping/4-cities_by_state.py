#!/usr/bin/python3
"""Script that lists all the cities
from the database hbtn_0e_4_usa"""


from sys import argv
import MySQLdb


def connect_mysql():
    """Connect to a MySQL server running on
    localhost at port 3306"""
    db = MySQLdb.connect(
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        host="localhost",
        port=3306
    )
    with db.cursor() as cur:
        cur.execute(
            "SELECT cities.id, cities.name, states.name \
            FROM cities \
            JOIN states \
            ON cities.state_id = states.id \
            ORDER BY cities.id ASC"
        )
        rows = cur.fetchall()
        if rows is not None:
            for row in rows:
                print(row)

if __name__ == "__main__":
    connect_mysql()
