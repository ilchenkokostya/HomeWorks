my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

i = -1

while i+1 < len(my_list):
    i += 1

    if my_list[i] > 0:
        print(my_list[i])
        continue

    if my_list[i] < 0:
        print("Встретилось отрицательное число:", my_list[i])
        break

print("Оброботка списка закончилась")





