class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = self.set_color(*color)  # цвет фигуры
        self._sides = self.set_sides(*sides)  # список сторон
        self.filled = False  # закрашенный, bool

    def get_color(self):
        return f'Cписок RGB цветов {self} {self.__color}'  # цвет фигуры

    @staticmethod
    def __is_valid_color(r, g, b):  # проверка цвета
        if 0 < r <= 255 and 0 < g <= 255 and 0 < b <= 255:  # Цвет корректный
            return True
        else:
            print(f'Неверный параметр цвета {r}, {g}, {b}, 0-255. Отмена изменений!')
            return False

    def set_color(self, r, g, b):  # установка цвета
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]  # список RGB цветов
            self.filled = True  # закрашенный
            return [r, g, b]
        else:
            return getattr(self, '__color', None)

    def __is_valid_sides(self, new_sides):
        if isinstance(self, Cube):  # проверка куба
            if len(new_sides) == 1:
                return True
            else:
                print(
                    f'Неверное количество сторон {self}, должна быть указана 1 сторона. Отмена изменений!')
                return False
        if len(new_sides) == self.sides_count:  # проверка количества сторон
            for i in new_sides:
                if type(i) is not int or i <= 0:  # целые и положительные числа
                    print(
                        f'Неверный параметр стороны {self} {i}, только целые и положительные числа. Отмена изменений!')
                    return False
            else:
                return True
        else:
            print(f'Неверное количество сторон {self}, должно быть {self.sides_count} стороны(а). Отмена изменений!')
            return False

    def get_sides(self):
        return f'Cписок сторон {self} {self._sides}'  # список сторон

    def set_sides(self, *new_sides):  # принимаем новые стороны
        if self.__is_valid_sides(new_sides):  # проверка количества сторон
            if isinstance(self, Cube):
                new_sides = [list(new_sides)[0]] * 12  # список сторон куба
                self._sides = new_sides
                return new_sides
            self._sides = list(new_sides)
            return list(new_sides)
        else:
            return getattr(self, '_sides', None)

    def __len__(self):  # периметр фигуры
        return sum(self._sides)


class Circle(Figure):
    sides_count = 1  # количество сторон

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if self._sides:
            self.__radius = self._sides[0] / (2 * 3.14)  # радиус круга
        else:
            self.__radius = 0

    def __str__(self):
        return 'круга'

    def get_square(self):  # площадь круга
        self.__radius = self._sides[0] / (2 * 3.14)
        return f'Площадь {self} {(self.__radius ** 2) * 3.14}'


class Triangle(Figure):
    sides_count = 3  # количество сторон

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):  # площадь треугольника
        p = (self._sides[0] + self._sides[1] + self._sides[2]) / 2
        return f'Площадь {self} {(p * (p - self._sides[0]) * (p - self._sides[1]) * (p - self._sides[2])) ** 0.5}'

    def __str__(self):
        return 'треугольника'


class Cube(Figure):
    sides_count = 12  # количество сторон

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_volume(self):  # площадь круга
        if self._sides:
            return f'Площадь {self} {6 * self._sides[0] * self._sides[0]}'
        else:
            return f'Площадь {self} {0}'

    def __str__(self):
        return 'куба'


if __name__ == '__main__':
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())

    # print('------------------Круг-------------------------------')
    # circle = Circle((200, 200, 111), 10, 22)
    # circle1 = Circle((200, 200, 111), 10)
    # print(circle1.get_color())
    # print(circle1.get_sides())
    # print(circle1.get_square())
    # circle1.set_sides(12)
    # print(circle1.get_sides())
    # print(circle1.get_square())
    # print('------------------Треугольник-------------------------------')
    # triangle = Triangle((2220, 35, 130), 10, 10, 10)
    # triangle1 = Triangle((222, 35, 130), 10, 10, 10)
    # print(triangle1.get_color())
    # print(triangle1.get_sides())
    # print(triangle1.get_square())
    # triangle1.set_sides(12, 12, 12)
    # print(triangle1.get_sides())
    # print(triangle1.get_square())
    # print('--------------------Куб-----------------------------')
    # cube1 = Cube((222, 35, 130), 10, 22)
    # print(cube1.get_color())
    # print(cube1.get_sides())
    # print(cube1.get_volume())
    # cube1.set_sides(12)
    # print(cube1.get_sides())
    # print(cube1.get_volume())
    # cube1.set_sides(12, 12)
