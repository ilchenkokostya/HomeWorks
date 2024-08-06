def gen_pwd(n):
    result = ""

    for i in range(1, n):
        for j in range(i + 1, n):
            if n % (i + j) == 0:
                result += str(i) + str(j) + ' '
    return result


num = 0
while num < 3 or num > 20:
    num = int(input("Введите число для пароля от 3 до 20: "))

pwd = gen_pwd(num)
print(f"Пароль для числа {num} - {pwd}")
