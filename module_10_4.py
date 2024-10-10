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

    def run(self):
        time.sleep(random.randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.queue = queue.Queue()
        self.tables = tables

    def guest_arrival(self, *guests):  # Добавление гостей в очередь
        for guest in guests:
            if any(table.is_free for table in self.tables):  # Если есть свободные столы
                free_table = next((table for table in self.tables if table.is_free), None)  # Поиск свободного стола
                free_table.guests = guest.name
                print(f'{guest.name} сел(-а) за стол номер {free_table.number}')
                guest.start()
                # guest.join()
            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):  # Обслуживание гостей
        while not self.queue.empty():
            queue_guest = self.queue.get()

            while not queue_guest.is_alive():
                for table in tables:
                    for guest in guests:
                        if guest.name == table.guests and not guest.is_alive():
                            print(f'{guest.name} покушал(-а) и ушёл(ушла)')
                            print(f'Стол номер {table.number} свободен')
                            table.guests = queue_guest.name
                            print(
                                f'{queue_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                            if not queue_guest.is_alive():
                                queue_guest.start()


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

    # # Заполнение кафе столами
    cafe = Cafe(*tables)
    #
    # # Приём гостей
    cafe.guest_arrival(*guests)

    # # Обслуживание гостей
    cafe.discuss_guests()
