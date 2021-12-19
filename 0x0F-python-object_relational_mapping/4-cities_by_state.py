#!/usr/bin/python3
"""script Lists all cities & is safe"""

import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities JOIN\
                states ON cities.state_id = states.id ORDER BY cities.id;")
    result = cur.fetchall()
    for row in result:
        print(row)
    cur.close()
    db.close()
