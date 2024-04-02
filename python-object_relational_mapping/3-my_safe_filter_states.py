#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the
'states' table of 'hbtn_0e_0_usa' where 'name' matches the argument.
Make sure it is safe fromm MySQL injections!
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
        SELECT *
        FROM states
        WHERE name = BINARY ?
        ORDER BY states.id ASC
    """, (state_name))

    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
