immutable_var = 5, 7, 6, True, "Privet"
print(immutable_var)

try:
    immutable_var[0] = 'figvam'
except:
    print("Кортежи в Python являются неизменяемыми структурами данных")

mutable_list = [11, 12, True, "Yes"]
print(mutable_list)
mutable_list[0] = 1
mutable_list[1] = 2
mutable_list[2] = False
mutable_list[3] = "No"
print(mutable_list)
