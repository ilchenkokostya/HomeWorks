def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print('-- 1.Функция с параметрами по умолчанию')
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

print('\n-- 2.Распаковка параметров')
values_list = [99, 'list', [1, 2, 3]]
print_params(*values_list)
values_dict = {'a':777, 'b':'dict', 'c':(4, 5, 6)}
print_params(**values_dict)

print('\n-- 3.Распаковка + отдельные параметры')
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)