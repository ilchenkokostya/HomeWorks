class Vehicle:  # любой транспорт
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner: str, _model: str, __color: str, __engine_power: int):
        self.owner = owner  # владелец
        self._model = _model  # модель
        if self.set_color(__color):  # проверка на валидность цвета
            self.__color = __color  # цвет
        else:
            self.__color = None
        self.__engine_power = __engine_power  # мощность двигателя

    def get_model(self):
        return self._model

    def get_horsepower(self):
        return self.__engine_power

    def get_color(self):
        return self.__color

    def set_color(self, color):  # сетер
        if color.lower() in self.__COLOR_VARIANTS:
            self.__color = color
            return True
        else:
            print(f'Нельзя сменить цвет на {color}')  # Вызов метода
            return False

    def print_info(self):
        print(f'---------\nМодель: {self.get_model()}')
        print(f'Мощность двигателя: {self.get_horsepower()}')
        print(f'Цвет: {self.get_color()}')
        print(f'Владелец: {self.owner}')


class Sedan(Vehicle):  # седан
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner: str, _model: str, __color: str, __engine_power: int, __passengers: int = 5):
        super().__init__(owner, _model, __color, __engine_power)
        if self.__check_passengers(__passengers):
            self.__passengers = __passengers  # кол-во пассажиров
        else:
            self.__passengers = None

    @classmethod
    def __check_passengers(cls, passengers):
        if passengers > cls.__PASSENGERS_LIMIT:
            print(f'В седане нельзя перевозить больше {cls.__PASSENGERS_LIMIT} пассажиров')
            return False
        else:
            return True

    def set_passengers(self, passengers):
        if self.__check_passengers(passengers):
            self.__passengers = passengers

    def get_passengers(self):
        return self.__passengers

    def print_info(self):
        super().print_info()
        print(f'Кол-во пассажиров: {self.get_passengers()} \n ---------')


if __name__ == '__main__':
    # Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500, 5)

    # Изначальные свойства
    vehicle1.print_info()

    # Меняем свойства (в т.ч. вызывая методы)
    vehicle1.set_color('Pink')
    vehicle1.set_color('BLACK')
    vehicle1.owner = 'Vasyok'

    vehicle1.set_passengers(10)
    # Проверяем что поменялось
    vehicle1.print_info()
