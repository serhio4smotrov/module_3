def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params()
print_params(5, 'try', False)
print_params(7)
#print_params(6, 'djf', True, True)  # ошибка при вызове, потому что передано больше аргументов, чем выделено
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = [True, 56, 'список']
values_dict = {'a': 58, 'b': 47.5, 'c': 'словарь'}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = ['список №', 2]
print_params(*values_list_2, 42)