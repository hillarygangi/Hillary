import sqlite3

conn = sqlite3.connect('example.db')
print("Opened database successfully")

conn.execute("INSERT INTO EMPLOYEES VALUES (1,'FAITH KARIMI',23,3450000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (2,'BOB KURIA',23,1150000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (3,'JANE MUTHONI',27,45000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (4,'MARY ANNE',38,2080000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (5,'PAUL KAMAU',45,450000.00)")

conn.commit()
print("Record inserted successfuly")
conn.close()