import sqlite3

def fill_bd(username, email, age, balanse, cursor):
    #User, example@gmail.com, 10, 1000
    count_name = 0
    try:
        for i in range(1,11):
            name = username
            mail = email
            sql_write= """INSERT INTO users
                                      (username, email, age, balance) VALUES (?, ?, ?, ?)"""
            name += str(i)
            mail += f'{str(i)}@gmail.com'
            age  += 10
            data = (name, mail, age, balanse)
            cursor.execute(sql_write, data)
            connection.commit()  # принять изменения
    except sqlite3.Error as err:
        print(err)
    return

def update_bd(cursor,connection):
    try:
        sql_update = """ UPDATE users SET balance = 500 WHERE id = ?"""
        for i in range (10):
            data = (i,)
            if i % 2 == 0:
                cursor.execute(sql_update,data)
        connection.commit()
    except sqlite3.Error as err:
        print(err)

def del_record(cursor, connection):
    try:
        sql_del = """ DELETE FROM users where id = ? """

        for i in  range (10):
            data = (i,)
            if i % 3 == 0:
                cursor.execute(sql_del, data)
        connection.commit()
    except sqlite3.Error as err:
        print(err)

def read_from_bd(cursor):
    sql_read = """ SELECT username, email, age, balance from Users WHERE age != 60"""
    cursor.execute(sql_read)
    records = cursor.fetchall()
    for i in records:
        name = i[0]
        email = i[1]
        age = i[2]
        balance = i[3]
        print(f'Имя: {name:^7}  | Почта: {email:^20} | Возраст: {age:^5} | Баланс: {balance}')

try:
    connection = sqlite3.connect('not_telegram.db')
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NO NULL,
            age INTEGER,
            balance INTEGER
        );
    ''')
    fill_bd('User', 'example',0, 1000, cursor)
    update_bd(cursor, connection)
    del_record(cursor, connection)
    read_from_bd(cursor)

except sqlite3.Error as err:
    print (err)
finally:
    if connection:
        connection.close()