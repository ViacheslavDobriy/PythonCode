# Реализовать алгоритм задания случайных чисел. Без использования встроенного генератора псевдослучайных чисел

import time

def random_time():
    return time.time()

def insert_user():
    return input('Insert any letter').lower()

def dictionary_of_letters(letter):
    dict = \
        {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'i': 9,
        'j': 10,
        'k': 11,
        'l': 12,
        'm': 13,
        'n': 14,
        'o': 15,
        'p': 16,
        'q': 17,
        'r': 18,
        's': 19,
        't': 20,
        'u': 21,
        'v': 22,
        'w': 23,
        'x': 24,
        'y': 25,
        'z': 26,
        }
    for _ in dict:
        if letter == _:
            print('If is working')
            return dict[_]

def modified_number(number):
    list = []
    result = 0
    mod_number = (number + 1)**3
    while mod_number > 0:
        list.append(mod_number//3)
        mod_number //= 3
    for _ in list:
        result += _
    return result

def negative_or_positive(time):
    if int(float(time)*1000000)%2 == 0:
        return 1
    else:
        return -1

# print(len(str(-time.time())))
# print(create_row(random_time()))
print(modified_number(dictionary_of_letters(insert_user()))*(negative_or_positive(random_time())))