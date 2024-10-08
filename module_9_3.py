# "Генераторные сборки"

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(x) - len(y) for x, y in zip(first, second) if len(x) - len(y))
print(list(first_result))

first_result = next(len(x) - len(y) for x, y in zip(first, second) if len(x) - len(y))
print(first_result)

second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))
print(list(second_result))

third_result = (len(value) == len(second[i]) for i, value in enumerate(first))
print(list(third_result))
