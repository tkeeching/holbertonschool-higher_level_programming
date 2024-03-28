#!/usr/bin/python3

import MySQLdb
import sys

def main():
    username, password, dbname = sys.argv[1:]

    conn = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=dbname, charset="utf8")

    cur = conn.cursor()

    cur.execute("SELECT * FROM states ORDER BY states.id ASC")

    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    conn.close()
