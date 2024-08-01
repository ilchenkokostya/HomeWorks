my_dict = {"Yaroslav": 1999, "Igor": 2005, "Dima": 1995}
print(my_dict)
print(my_dict.get("Dima"))
print(my_dict.get("Victor"))
my_dict.update({"Misha": 1998, "Ruslan": 1999})
a = my_dict.pop(('Igor'))
print(a)
print(my_dict)
print('\n')

my_set = {5, 6, 9, 5, 9, 4, 3, 5, 6, 6, True, 'blue', True, 'blue'}
print(my_set)
my_set.add((88, 100))
my_set.add(7)
my_set.remove(3)
print(my_set)
