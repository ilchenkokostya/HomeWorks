first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))

if first == second == third:
    print(' 3 одинаковых числа ')
elif first == second or first == third or second == third:
    print(' 2 одинаковых числа ')
else:
    print(' Нет одинаковых чисел ')