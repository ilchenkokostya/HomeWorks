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

# cursor.execute('''
#                SELECT "Имя: "||username||" | Почта: "||email||" | Возраст: "||age||" | Баланс: "||balance as info
#                        FROM Users
#                        WHERE age <> 60
#                ''')

cursor.execute('DELETE FROM Users WHERE id = 6')

cursor.execute('''
               SELECT COUNT(*) FROM Users 
               ''')
total_users = cursor.fetchone()
print(f'Кол-во пользователей: {total_users[0]}')

cursor.execute('''
               SELECT SUM(balance) FROM Users
               ''')
all_balances = cursor.fetchone()
print(f'Cумма всех балансов: {all_balances[0]}')
print(f'Cредний баланс: {all_balances[0] / total_users[0]}')

connection.commit()
connection.close()
