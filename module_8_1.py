def handler_errors(func):
    def wrapper(a, b):
        try:
            return func(a, b)
        except TypeError as exc:
            return str(a) + str(b)
        except ZeroDivisionError as exc:
            return 'Деление на ноль'

    return wrapper


@handler_errors
def add_everything_up(a, b):
    return f'{a + b:.3f}'


@handler_errors
def div_zero_everything(a, b):
    return f'{a / b:.3f}'


if __name__ == "__main__":
    print(add_everything_up(123.456, 'строка'))
    print(add_everything_up('яблоко', 4215))
    print(add_everything_up(123.456, 7))

    print(div_zero_everything(101, 0))
