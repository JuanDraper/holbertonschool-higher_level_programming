#!/usr/bin/python3
# Lists all states from the database 
import MySQLdb
import sys
if __name__ == "__main__":
    dbase = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cr = dbase.cursor()
    cr.execute("SELECT * FROM states ORDER BY states.id;")
    rt = cr.fetchall()
    for row in rt:
        print(row)
    cr.close()
    dbase.close()
