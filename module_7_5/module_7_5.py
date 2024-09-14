import os
import time

directory = os.getcwd()
print('Текущая директория: ', directory)

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)  # формирования полного пути к файлам
        filetime = os.path.getmtime(filepath)  # формирования времени изменения файла
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)  # формирования размера файла
        parent_dir = os.path.dirname(filepath)  # формирования родительской директории

        print(
            f'Обнаружен файл: {file}\n Путь: {filepath}\n Размер: {filesize} байт'
            f'\n Время изменения: {formatted_time}\n Родительская директория: {parent_dir}')
