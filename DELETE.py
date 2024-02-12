import sqlite3

conn = sqlite3.connect('example.db')
print("Opened database successfully")

conn.execute("DELETE FROM EMPLOYEES WHERE ID=1")
conn.commit()