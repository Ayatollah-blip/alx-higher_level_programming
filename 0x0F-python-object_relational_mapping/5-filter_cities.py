#!/usr/bin/python3

"""

This script lists all states from the

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
    cur.execute("""SELECT cities.name from cities
                JOIN states ON cities.state_id = states.id
                WHERE states.name=%(state)s ORDER BY cities.id ASC""",
                {'state': argv[4]})
    row_select = cur.fetchall()

    if len(row_select) != 0:
        for i in range(len(row_select)-1):
            print(row_select[i][0], end=", ")
        print(row_select[i+1][0])

    cur.close()
    db.close()
