grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

sort_students = sorted(list(students))
avg_dict = {}

for i in range(len(grades)):
     avg_dict[sort_students[i]] = (sum(grades[i])/len(grades[i]))

print(avg_dict)
