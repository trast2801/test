import sqlite3

def initiate_db(cursor):
    cursor.execute(''' CREATE TABLE IF NOT EXISTS Products (
              id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
              title TEXT NOT NULL,
              description TEXT,
              price INTEGER NOT NULL        
           );
    ''')
    return

def get_all_products(cursor):

     sql_qst = """SELECT title, description, price, id FROM Products """
     try:
        cursor.execute(sql_qst)
        records = cursor.fetchall()
        return records
     except sqlite3.Error as err:
         print(err)
         return None


