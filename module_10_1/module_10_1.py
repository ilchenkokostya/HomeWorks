# "Создание потоков"

import threading
import time
from datetime import datetime


def write_words(word_count, file_name):
    with open(file_name, "w", encoding="utf-8") as file:
        for i in range(word_count):
            file.write(f"Какое-то слово № {i + 1}\n")
            time.sleep(0.01)
    print(f"Завершилась запись в файл {file_name}")


if __name__ == "__main__":
    time_start = datetime.now()
    write_words(10, 'example1.txt')
    write_words(30, 'example2.txt')
    write_words(200, 'example3.txt')
    write_words(100, 'example4.txt')
    time_end = datetime.now()
    time_delta = time_end - time_start
    print(f"--Время работы функций: {time_delta}")

    time_start = datetime.now()
    t1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
    t2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
    t3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
    t4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

    time_end = datetime.now()
    time_delta = time_end - time_start
    print(f"---Время работы потоков: {time_delta}")
