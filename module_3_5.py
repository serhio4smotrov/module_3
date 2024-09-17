def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    elif first == 0:
        return 1
    else:
        return first


result_1 = get_multiplied_digits(5060)
result_2 = get_multiplied_digits(8402)
print(f'{result_1}, {result_2}')