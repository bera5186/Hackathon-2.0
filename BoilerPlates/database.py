"""
5 steps for working with SqLite3 databse : 
1. Connect to database
2. Create a cursor object
3. Write an SQL querry
4. Commit changes
5. Close database connection

"""
import sqlite3


conn = sqlite3.connect("data.db")
cur  = conn.cursor()
cur.execute("CREATE TABLE store(item TEXT, quantity INTEGER, price REAL) ")
conn.commit()
conn.close()