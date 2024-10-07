# Блокировки и обработка ошибок

import threading
import time
import random


class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self, amount):
        self.balance += amount
        print(f"Пополнение: {amount}. Баланс: {self.balance}")
        if self.balance >= 500 and self.lock.locked():
            self.lock.release()
        time.sleep(0.001)

    def take(self, amount):
        print(f'Запрос на {amount}')
        if amount < self.balance:
            self.balance -= amount
            print(f"Снятие: {amount}. Баланс: {self.balance}")
        else:
            print(f'Запрос отклонён, недостаточно средств')
            if not self.lock.locked():
                self.lock.acquire()


bk = Bank()

for i in range(100):
    th1 = threading.Thread(target=bk.deposit, args=(random.randint(50, 500),))
    th2 = threading.Thread(target=bk.take, args=(random.randint(50, 500),))

    th1.start()
    th2.start()

    th1.join()
    th2.join()

#############################################
# threads = []
# threads += [threading.Thread(target=bk.deposit, args=(random.randint(50, 500),)) for _ in range(100)]
# threads += [threading.Thread(target=bk.take, args=(random.randint(50, 500),)) for _ in range(100)]
# [t.start() for t in threads]
# [t.join() for t in threads]

print(f'Итоговый баланс: {bk.balance}')
