class House:

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor <= self.number_of_floors:
            print(f"Идём {self.name} на {new_floor} этаж")
            for i in range(new_floor):
                print(i + 1)
        else:
            print(f"Такого этажа не существует в {self.name}")


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
