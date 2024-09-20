def add_everything_up(a, b, op="+"):
    if op == "+":
        try:
            return round((a + b), 4)
        except TypeError as exc:
            return str(a) + str(b)
    if op == "/":
        try:
            return round((a / b), 4)
        except ZeroDivisionError:
            return "На ноль делить нельзя"


if __name__ == "__main__":
    print(add_everything_up(123.456, 'строка'))
    print(add_everything_up('яблоко', 4215))
    print(add_everything_up(123.456, 7))

    print(add_everything_up(101, 0, '/'))
