#!/usr/bin/python3

"""

This script lists all states with name with N from the

database `hbtn_0e_0_usa`.

"""

import MySQLdb
from sys import argv


def makingConnection(userName, password, name):
    return MySQLdb.connect(
        host="localhost",
        user=userName,
        port=3306,
        passwd=password,
        db=name)


if __name__ == '__main__':

    """
    Access to the database and get the states
    from the database.
    """
    db = makingConnection(argv[1], argv[2], argv[3])
    cur = db.cursor()
    cur.execute("""SELECT * from states
                WHERE name LIKE BINARY '{}'
                ORDER BY states.id ASC""".format(argv[4]))
    row_select = cur.fetchall()
    for table in cur:
        print(table)
    cur.close()
    db.close()
