import sqlite3

def initiate_db(cursor):
    cursor.execute(''' CREATE TABLE IF NOT EXISTS Products (
              id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
              title TEXT NOT NULL,
              description TEXT,
              price INTEGER NOT NULL        
           );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NO NULL,
            age INTEGER,
            balance INTEGER
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
def add_user(username, email, age):
    pass

def is_included(username,cursor):
    sql_qst = """ SELECT EXISTS(SELECT * FROM users where username = ?)"""
    data = (username,)
    cursor.execute(sql_qst,data)
    records = cursor.fetchone()
    if records[0] == 1:
        return True
    else:
        return False


def add_user(username, email, age, cursor):
    sql_qst = """ INSERT INTO users (username,email,age, balance) VALUES (?,?,?,?)"""
    #if is_included(username,cursor):
    data = (username, email, age, 1000)
    cursor.execute(sql_qst, data)
#    return True
    #else:
    #    return False