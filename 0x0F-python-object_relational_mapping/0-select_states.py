import MySQLdb

def makingConnection(userName, password, name):
    return MySQLdb.connect(user=userName, passwd=password, db=name)

if __name__ == '__main__':
    db = makingConnection("me", "me", "hbtn_0e_0_usa")
    cur = db.cursor()
    cur.execute("SELECT * from states")
    for table in cur:
        print(table)
