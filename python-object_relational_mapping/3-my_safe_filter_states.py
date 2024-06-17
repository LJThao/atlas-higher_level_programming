#!/usr/bin/python3
"""Script that takes in arguments and displays all values
in the states table of hbtn_0e_0_usa where name matches
the argument. Then, write one that is safe from the
MySQL injections."""


from sys import argv
import MySQLdb


def connect_mysql():
    """Connect to a MySQL server running on localhost
    at port 3306"""
    db = MySQLdb.connect(
        user=argv[1],
        passwd =argv[2],
        db=argv[3],
        host="localhost",
        port=3306
    )

    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states \
        WHERE name LIKE BINARY %(name)s \
        ORDER BY states.id ASC", {'name': argv[4]}
        )
    rows = cur.fetchall()
    for row in rows:
        print(row)

if __name__ == "__main__":
    connect_mysql()
