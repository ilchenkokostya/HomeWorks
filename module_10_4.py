# Очереди для обмена данными между потоками.
import random
from threading import Thread
import time
import queue


class Table:
    def __init__(self, number):
        self.number = number  # Номер стола
        self.guests = None  # Гость за ним

    @property
    def is_free(self):
        return self.guests is None


class Guest(Thread):  # Гость
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.eat = False  # Поел или нет

    def run(self):
        time.sleep(random.randint(3, 10))

    @property
    def is_not_eat(self):
        return self.eat is False  # Не поел


class Cafe:
    def __init__(self, *tables):
        self.queue = queue.Queue()
        self.tables = tables
        self.cafe_zal = {}

    def guest_arrival(self, *guests):  # Приём гостей

        for guest in guests:
            free_table = next((table for table in self.tables if table.is_free), None)  # Поиск свободного стола
            if free_table:
                free_table.guests = guest.name
                print(f'{guest.name} сел(-а) за стол номер {free_table.number}')
                self.cafe_zal[free_table] = guest  # Добавление гостя в кафе
                guest.eat = True
                guest.start()
                # guest.join()
            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):  # Обслуживание гостей
        join_guest = []
        while not self.queue.empty():
            queue_guest = self.queue.get()

            while queue_guest.is_not_eat:  # Пока гость не поел
                for free_table, free_guest in self.cafe_zal.items():  # бегаем по кафе
                    if not free_guest.is_alive():
                        print(f'{free_guest.name} покушал(-а) и ушёл(ушла)')
                        print(f'Стол номер {free_table.number} свободен')
                        print(f'{queue_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {free_table.number}')
                        free_table.guests = queue_guest.name
                        queue_guest.eat = True
                        self.cafe_zal[free_table] = queue_guest
                        queue_guest.start()
                        join_guest.append(queue_guest)
                        break
        else:
            [t.join() for t in join_guest]
            print('Все гости вышли из кафе')


if __name__ == '__main__':
    # Создание столов
    tables = [Table(number) for number in range(1, 6)]
    # Имена гостей
    guests_names = [
        'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
        'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
    ]
    # Создание гостей

    guests = [Guest(name) for name in guests_names]

    # print(*guests)

    # Заполнение кафе столами
    cafe = Cafe(*tables)

    # Приём гостей
    cafe.guest_arrival(*guests)

    # Обслуживание гостей
    cafe.discuss_guests()
