#!/usr/bin/python3
"""
Script that deletes all 'State' objects with a name
containing the letter 'a' from the database 'hbtn_0e_6_usa'
"""

from model_state import State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def add_state(username, password, db_name):
    """Deletes all State objects containing the letter 'a'"""
    # Create the engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, db_name))

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query the state objects containing letter 'a'
    state_to_delete = session.query(State).filter(State.name.like('%a%')).all()

    # Check if the state object exists
    if state_to_delete:
        # Delete each state object
        for state in state_to_delete:
            session.delete(state)

        # Commit the session to save the changes to the database
        session.commit()
    else:
        print('State not found')

    # Close the session
    session.close()


if __name__ == "__main__":
    username, password, db_name = sys.argv[1:]

    add_state(username, password, db_name)
