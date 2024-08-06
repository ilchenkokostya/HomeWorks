def calculate_structure_sum(*data):
    total_sum = 0
    # если элемент число и строка тогда суммируем их
    if isinstance(*data, str):
        total_sum += len(*data)
    elif isinstance(*data, int):
        total_sum += int(*data)
    else:  # если элемент не число и не строка, то проходим дальше
        for i in range(len(data)):
            # список
            if isinstance(data[i], list):
                for element in data[i]:
                    total_sum += calculate_structure_sum(element)
            # словарь
            if isinstance(data[i], dict):
                for element in data[i].items():
                    total_sum += calculate_structure_sum(element)
            # картеж
            if isinstance(data[i], tuple):
                for element in data[i]:
                    total_sum += calculate_structure_sum(element)
            # множество
            if isinstance(data[i], set):
                for element in data[i]:
                    total_sum += calculate_structure_sum(element)
    return total_sum


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(calculate_structure_sum(data_structure))