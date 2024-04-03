#!/usr/bin/python3
"""
Script that changes the name of a 'State'
object from the database 'hbtn_0e_6_usa'
"""

from model_state import State, Base
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def add_state(username, password, db_name):
    """Update the State object with id = 2"""
    # Create the engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, db_name))

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query the state object by id
    state_to_update = session.query(State).filter_by(id=2).first()

    # Check if the state object exists
    if state_to_update:
        # Update the name attribute
        state_to_update.name = 'New Mexico'

        # Commit the session to save the changes to the database
        session.commit()
    else:
        print('State not found')

    # Close the session
    session.close()


if __name__ == "__main__":
    username, password, db_name = sys.argv[1:]

    add_state(username, password, db_name)
