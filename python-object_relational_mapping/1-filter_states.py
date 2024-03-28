#!/usr/bin/python3
"""
Script that lists all 'states' with a 'name'
starting with 'N' from the database
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
        SELECT *
        FROM states
        WHERE name LIKE 'N%'
        ORDER BY states.id ASC
    """)

    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
