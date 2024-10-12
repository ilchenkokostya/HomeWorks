# Многопроцессное программирование
import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r') as f:
        while line := f.readline():
            all_data.append(line)


if __name__ == '__main__':
    # Линейный вызов
    start = datetime.datetime.now()
    for i in range(1, 5):
        read_info(f'file {i}.txt')
    end = datetime.datetime.now()
    print(end - start, '(линейный)')

    # Многопроцессный
    filenames = [f'./file {number}.txt' for number in range(1, 5)]
    with multiprocessing.Pool(processes=4) as pool:
        start = datetime.datetime.now()
        pool.map(read_info, filenames)
    end = datetime.datetime.now()
    print(end - start, '(многопроцессный)')
