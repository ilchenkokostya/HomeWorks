import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY,
        username  TEXT NOT NULL,
        email TEXT  NOT NULL,
        age INTEGER,
        balance INTEGER NOT NULL
        )''')

cursor.execute('DELETE FROM Users')

for i in range(1, 11):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?,?,?,?)',
                   (f'User{i}', f'example{i}@gmail.com', f'{i * 10}', f'1000'))

cursor.execute('''
                UPDATE Users SET balance = 500
                       WHERE id % 2 != 0      
               ''')

cursor.execute('''
               DELETE FROM Users
                       WHERE (id+2) % 3 = 0  
               ''')

cursor.execute('''
               SELECT "Имя: "||username||" | Почта: "||email||" | Возраст: "||age||" | Баланс: "||balance as info
                       FROM Users
                       WHERE age <> 60
               ''')
users = cursor.fetchall()
for user in users:
    print(user[0])

connection.commit()
connection.close()
