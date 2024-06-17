#!/usr/bin/python3
"""Script that lists all states from the database
hbtn_0e_0_usa"""


from sys import argv
import MySQLdb


def connect_mysql():
    """Connect to MySQL server running on
    localhost at port 3306"""
    db = MySQLdb.connect(
        user=argv[1],
        passwd=argv[2], 
        db=argv[3], 
        host="localhost",
        port = 3306
        )

    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    states = cur.fetchall()
    for state in states:
        print(state)

if __name__ == '__main__':
    connect_mysql()
