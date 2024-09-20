def personal_sum(numbers):
    incorrect_data, result = 0, 0
    for number in numbers:
        try:
            result += number
        except TypeError:
            print(f'Некорректный тип данных для подсчёта суммы - {number}')
            incorrect_data += 1
    return result, incorrect_data


def calculate_average(numbers):
    try:
        summ, incorrect_data = personal_sum(numbers)
        if len(numbers) != incorrect_data:  # Если в коллекции есть корректные значения
            return summ / (len(numbers) - incorrect_data)
        else:
            return 0
    except ZeroDivisionError:
        print('Коллекция numbers пустая')
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None


if __name__ == '__main__':
    print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
    print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
    print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
    print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
