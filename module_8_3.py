class IncorrectVinNumber(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


class IncorrectCarNumbers(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        self.__vin = self.__is_valid_vin(vin)
        self.__numbers = self.__is_valid_numbers(numbers)

    def __str__(self):
        return f'{self.model}, вин: {self.__vin}, номер: {self.__numbers}'

    @staticmethod
    def __is_valid_vin(vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер:', f'({vin_number})')
        if not (1000000 <= vin_number <= 9999999):
            raise IncorrectVinNumber('Неверный диапазон для vin номера:', f'({vin_number})')
        return vin_number

    @staticmethod
    def __is_valid_numbers(numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров:', f'({numbers})')
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера:', f'({numbers})')
        return numbers


if __name__ == '__main__':
    try:
        first = Car('Model1', 1000000, 'f123dj')
    except IncorrectVinNumber as exc:
        print(exc.message, exc.value)
    except IncorrectCarNumbers as exc:
        print(exc.message, exc.value)
    else:
        print(f'{first.model} успешно создан')
        print(first)

    try:
        second = Car('Model2', 300, 'т001тр')
    except IncorrectVinNumber as exc:
        print(exc.message, exc.value)
    except IncorrectCarNumbers as exc:
        print(exc.message, exc.value)
    else:
        print(f'{second.model} успешно создан')
        print(second)

    try:
        third = Car('Model3', 2020202, 'нет номера')
    except IncorrectVinNumber as exc:
        print(exc.message, exc.value)
    except IncorrectCarNumbers as exc:
        print(exc.message, exc.value)
    else:
        print(f'{third.model} успешно создан')
        print(third)
