#!/usr/bin/python3
"""
Script that lists all 'State' objects that contain
the letter 'a' from the database 'hbtn_0e_6_usa'
"""

from model_state import State, Base
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def list_states(username, password, db_name):
    """List all State objects from the database hbtn_0e_6_usa"""
    # Create the engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, db_name))

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query to get all State objects sorted by id
    states = session.query(State).filters(State.name.like('%a%')).order_by(State.id).all()

    # Display the results
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()


if __name__ == "__main__":
    username, password, db_name = sys.argv[1:]

    list_states(username, password, db_name)
