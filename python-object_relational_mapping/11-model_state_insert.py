#!/usr/bin/python3
"""
Script that adds the 'State' object 'Louisiana'
to the database 'hbtn_0e_6_usa'
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

    # Create a new State object
    new_state = State(name='Louisiana')

    # Add the new State object to the session
    session.add(new_state)

    # Commit the session to save the changes to the database
    session.commit()

    print(new_state.id)

    # Close the session
    session.close()


if __name__ == "__main__":
    username, password, db_name, state_name = sys.argv[1:]

    list_states(username, password, db_name)
