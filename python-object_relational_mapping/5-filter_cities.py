#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all
'cities' of that state, using the database 'hbtn_0e_4_usa'
"""

import MySQLdb
import sys


def main():
    username, password, dbname, state_name = sys.argv[1:]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname,
        charset="utf8")

    cur = conn.cursor()

    cur.execute("""
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = BINARY %s
        ORDER BY cities.id ASC
    """, (state_name,))

    query_rows = cur.fetchall()

    result = [row[0] for row in query_rows]
    print(result)

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
