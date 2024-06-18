#!/usr/bin/python3
"""Script that deletes all State
objects with a name containing the
letter a from the database hbtn_0e_6_usa"""


from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base
from model_state import State


def connect_mysql():
    """Connect to a MySQL server running
    on localhost at port 3306 with an ORM"""
    db = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1],
        argv[2],
        argv[3]
    )

    engine = create_engine(db)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State).filter(State.name.like('%a%'))
    rows = query.all()
    for row in rows:
        session.delete(row)
    session.commit()
    session.close()


if __name__ == "__main__":
    connect_mysql()
