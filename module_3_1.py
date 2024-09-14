calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()


def is_containce(string, list):
    count_calls()
    for i in list:
        if string.lower() == i.lower():
            return True
    return False


print(string_info('Карусель'))
print(string_info('Мореход'))
print(is_containce('Петрушка', ['укроп', 'редис', 'петрушка']))
print(is_containce('Лимон', ['Яблоко', 'ананас']))
print(string_info('цапля'))
print(calls)