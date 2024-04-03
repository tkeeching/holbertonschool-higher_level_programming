#!/usr/bin/python3
"""
Script that prints all 'City' objects from the database 'hbtn_0e_6_usa'
"""

from model_state import State
from model_city import City
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def list_cities(username, password, db_name):
    """List all City objects from the database hbtn_0e_6_usa"""
    # Create the engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, db_name))

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query to get all City objects sorted by id
    cities = session.query(City).order_by(City.id).all()

    # Display the results
    for city in cities:
        state_name = (session
                      .query(State)
                      .filter_by(id=city.state_id)
                      .first()
                      .name)
        print("{}: ({}) {}".format(state_name, city.id, city.name))

    # Close the session
    session.close()


if __name__ == "__main__":
    username, password, db_name = sys.argv[1:]

    list_cities(username, password, db_name)
