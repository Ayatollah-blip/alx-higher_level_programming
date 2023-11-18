#!/usr/bin/python3
"""

This script lists all states from the

database `hbtn_0e_0_usa`.

"""

import MySQLdb
from sys import argv

def makingConnection(userName, password, name):
    return MySQLdb.connect(host = "localhost", user=userName, port = 3306, passwd=password, db=name)

if __name__ == '__main__':
    db = makingConnection(argv[1], argv[2], argv[3])
    cur = db.cursor()
    cur.execute("SELECT * from states ORDER BY id ASC")
    row_select = cur.fetchall()
    for table in cur:
        print(table)
    cur.close()
    db.close()
