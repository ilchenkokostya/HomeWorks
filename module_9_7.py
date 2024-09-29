# Задание: Декораторы в Python
def is_prime(func):
    def wrapper(a, b, c):
        suma = func(a, b, c)
        if type(suma) is int and suma > 1:
            if any((suma % i == 0) for i in range(2, int(suma ** 0.5) + 1)):
                return f'Составное \n{suma}'
            else:
                return f'Простое \n{suma}'
        else:
            return f'Входные параметры: натуральные числа и сумма больше единицы'

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


if __name__ == '__main__':
    result = sum_three(2, 3, 6)
    print(result)
