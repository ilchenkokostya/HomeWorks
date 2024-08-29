class Plant:
    """ растения """

    def __init__(self, name: str, edible=False):
        self.edible = edible
        self.name = name


class Animal:
    """ животные """

    def __init__(self, name: str, alive=True, fed=False):
        self.alive = alive
        self.fed = fed
        self.name = name

    def eat(self, food):
        if food.edible:
            return print(f'{self.name} съел {food.name}')
        else:
            self.alive = False  # погиб
            return print(f'{self.name} не стал есть {food.name}')


class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Flower(Plant):
    pass


class Fruit(Plant):
    def __init__(self, name: str, edible=True):
        super().__init__(name)
        # self.name = name
        self.edible = edible


if __name__ == '__main__':
    a1 = Predator('Волк с Уолл-Стрит')
    a2 = Mammal('Хатико')
    p1 = Flower('Цветик семицветик')
    p2 = Fruit('Заводной апельсин')

    print(a1.name)
    print(p1.name)

    print(a1.alive)
    print(a2.fed)
    a1.eat(p1)
    a2.eat(p2)
    print(a1.alive)
    print(a2.fed)
