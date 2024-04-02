#!/usr/bin/python3
"""
Script that lists all 'cities' from the database 'hbtn_0e_4_usa'
"""

import MySQLdb
import sys


def main():
    username, password, dbname = sys.argv[1:]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname,
        charset="utf8")

    cur = conn.cursor()

    cur.execute("""
        SELECT cities.id, cities.name states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """)

    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
