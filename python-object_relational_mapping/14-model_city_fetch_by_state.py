#!/usr/bin/python3
"""Script that prints all City objects
from the database hbtn_0e_14_usa:"""


from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base
from model_state import State
from model_city import City


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
    query = session.query(State.name, City.id, City.name).\
        join(City, State.id == City.state_id).order_by(City.id)
    rows = query.all()
    for row in rows:
        print("{:s}: ({:d}) {:s}".format(*row))
    session.commit()
    session.close()


if __name__ == "__main__":
    connect_mysql()
