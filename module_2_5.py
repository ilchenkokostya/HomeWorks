def get_matrix(n, m, value):
    matrix = []

    # for i in range(n):
    #    matrix.append([value]*m)

    for i in range(n):
        matrix_2 = []
        for j in range(m):
           matrix_2.append(value)
        matrix.append(matrix_2)

    return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)