class House:

    def __init__(self, name, number_of_floors: int):
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self):
        return f"Название: {self.name} кол-во этажей: {self.number_of_floors}"

    def check(self, other):
        if not isinstance(other, (int, House)):
            raise TypeError(f"Параметр {other} должен быть типа int или House")
        if isinstance(other, House):
            other = other.number_of_floors
        return other

    def __eq__(self, other):  # ==
        return self.number_of_floors == self.check(other)

    def __lt__(self, other):  # <
        return self.number_of_floors < self.check(other)

    def __le__(self, other):  # <=
        return self.number_of_floors <= self.check(other)

    def __gt__(self, other):  # >
        return self.number_of_floors > self.check(other)

    def __ge__(self, other):  # >=

        return self.number_of_floors >= self.check(other)

    def __ne__(self, other):  # !=
        return self.number_of_floors != self.check(other)

    def __add__(self, other):  # +
        return House(self.name, self.number_of_floors + self.check(other))

    def __radd__(self, other):  # cправо +
        return self + other

    def __iadd__(self, other):  # +=
        return self + other


if __name__ == '__main__':
    h1 = House('ЖК Эльбрус', 10)
    h2 = House('ЖК Акация', 20)

    print(h1)
    print(h2)

    print(h1 == h2)  # __eq__

    h1 = h1 + 10  # __add__
    print(h1)
    print(h1 == h2)

    h1 += 10  # __iadd__
    print(h1)

    h2 = 10 + h2  # __radd__
    print(h2)

    print(h1 > h2)  # __gt__
    print(h1 >= h2)  # __ge__
    print(h1 < h2)  # __lt__
    print(h1 <= h2)  # __le__
    print(h1 != h2)  # __ne__

    h1 = h1 + h2 + 999
    print(h1)
