def calculate_structure_sum(*data):
    total_sum = 0
    # если элемент число и строка тогда суммируем их
    if isinstance(*data, str):
        total_sum += len(*data)
    elif isinstance(*data, int):
        total_sum += int(*data)
    else:  # если элемент не число и не строка, то проходим дальше
        for i in range(len(data)):
            # список кортеж множество
            if isinstance(data[i], (list, tuple, set)):
                for element in data[i]:
                    total_sum += calculate_structure_sum(element)
            # словарь
            if isinstance(data[i], dict):
                for element in data[i].items():
                    total_sum += calculate_structure_sum(element)
    return total_sum


data_structure = [
    [1, 2, 3, ''],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(calculate_structure_sum(data_structure))


# второй вариант
# ---------------------------
def calculate_structure_sum(*args):
    summa = 0
    for item in args:
        if isinstance(item, (list, set, tuple)):
            for element in item:
                summa += calculate_structure_sum(element)
        if isinstance(item, dict):
            for key, value in item.items():
                summa += calculate_structure_sum(key, value)
        if isinstance(item, str):
            summa += len(item)
        if isinstance(item, int):
            summa += item
    return summa


data_structure = [
    [1, 2, 3, ''],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(calculate_structure_sum(data_structure))
