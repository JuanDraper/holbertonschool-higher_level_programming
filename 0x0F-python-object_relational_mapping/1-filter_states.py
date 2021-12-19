#!/usr/bin/python3
"""  Lists all states starting with N."""
import MySQLdb
import sys
if __name__ == "__main__":
    dbase = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cr = dbase.cursor()
    cr.execute("SELECT * FROM states ORDER BY id;")
    rt = cur.fetchall()
    for row in rt:
        if row[1].startswith("N"):
            print(row)
    cr.close()
    dbase.close()
