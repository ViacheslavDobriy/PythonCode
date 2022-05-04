# Найти произведение пар чисел в списке. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 

import math

def generate_list():
    '''Function for generate list. It returns list'''
    list = [2, 3, 4, 5, 6, 7, 8, 10, 13]
    return list

def prepare_new_list(basic_list):
    '''Function take list like argument and return two times less len of that. It returns len for new list of numbers'''
    len_res_list = math.ceil(len(basic_list)/2)
    return len_res_list

def generate_result_list(basic_list, len_of_list):
    '''This function create a new list and take two arguments to definite elements for that: basic_list and len of result list. It returns result list.'''
    result_list = []
    for count, elem in enumerate(basic_list):
        if len(result_list) != len_of_list:
            temp = basic_list[count]*basic_list[-1-count]
            result_list.append(temp)
    return result_list

print(generate_result_list(generate_list(), prepare_new_list(generate_list())))