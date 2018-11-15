"""
5 steps for working with SqLite3 databse : 
1. Connect to database
2. Create a cursor object
3. Write an SQL querry
4. Commit changes
5. Close database connection

"""
import sqlite3


def create():
    """
    Function to create database.
    """
    conn = sqlite3.connect('data.db')
    curr = conn.cursor()
    curr.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()


def insert(item, quantity, price):
    """
    Taking Values From the users.
    """
    try:
        conn = sqlite3.connect("data.db")
        cur  = conn.cursor()
        cur.execute("INSERT INTO STORE VALUES(?, ?, ?)", (item, quantity, price))
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)

def veiw():
    """
    Function for viewing the data inside of a database.
    """
    conn = sqlite3.connect("data.db")
    cur  = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(item):
    """
    Function to delete an item
    """

    conn = sqlite3.connect("data.db")
    cur  = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?", (item,))
    conn.commit()
    conn.close()


create()
#insert('Apple-Juice', 100, 15)
#insert()
print(veiw())
#delete("juice")