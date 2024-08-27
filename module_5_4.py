class House:
    houses_history = []

    def __new__(cls, name, number_of_floors):  # Инициализатор
        cls.houses_history.append(name)
        return object.__new__(cls)

    def __init__(self, name: str, number_of_floors: int):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):  # Финализатор
        print(f"{self.name} снесён, но он останется в истории")


if __name__ == '__main__':
    h1 = House('ЖК Эльбрус', 10)
    print(House.houses_history)
    h2 = House('ЖК Акация', 20)
    print(House.houses_history)
    h3 = House('ЖК Матрёшки', 20)
    print(House.houses_history)

    # Удаление объектов
    del h2
    del h3

    print(House.houses_history, '*')
