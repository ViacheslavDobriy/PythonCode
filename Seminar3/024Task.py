# В заданном списке вещественных чисел найдите разницу между максимальным
# и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

numbers_list = [1.1, 1.2, 3.5, 5, 10.01]


def get_decimal_part(starting_list, int_digits_after_point):
    '''Function take two arguments - starting list and numbers digits after dot. It returns list of decimal parts.'''
    list_of_decimal_part = []
    for i in range(0, len(starting_list)):
        list_of_decimal_part.append(round((starting_list[i] % 1), int_digits_after_point))
    return list_of_decimal_part


def max_decimal_part(list):
    '''Function take one argument: list. Function is running through list and find a maximum element and returns it'''
    max = list[0]
    for i in range(0, len(list)):
        if max < list[i]:
            max = list[i]
    return max


def min_decimal_part(list):
    '''Function take one argument: list. Function is running through list and find a minimum element and returns it'''
    min = list[0]
    for i in range(0, len(list)):
        if min > list[i] and list[i] != 0:
            min = list[i]
    return min

def diff_between_max_min(a, b):
    '''Function can determinate difference between a and b. And it returns positive number'''
    result = a - b
    if result >= 0:
        return result
    else:
        return -result

print(diff_between_max_min(max_decimal_part(get_decimal_part(numbers_list, 2)), min_decimal_part(get_decimal_part(numbers_list, 2))))