# Строка содержит набор чисел. Показать большее и меньшее число
# Символ-разделитель - пробел


def insert_number():
    '''Function let user to insert row of numbers, and returns string value'''
    return str(input('Insert numbers'))


def string_int(user_number):
    '''Function take string value like an argument and modify it in list. It returns list of integer values'''
    return [int(x) for x in user_number.split(' ')]


def Maximum(string):
    '''Functon have only one argument - list of integer values. Here program is looking for maximum and returns it'''
    max = string[0]
    for i in range(0, len(string)):
        if string[i] > max:
            max = string[i]
    return max


def Minimum(string_of_numbers):
    '''Functon have only one argument - list of integer values. Here program is looking for minimum and returns it'''
    min = string_of_numbers[0]
    for i in range(0,len(string_of_numbers)):
        if string_of_numbers[i] < min:
            min = string_of_numbers[i]
    return min

def Create_Row(max_str, min_str):
    '''Function is getting two int values - minimum and maximum and create a list which consists of these two values and space between. '''
    result = []
    result.append(max_str)
    result.append(' ')
    result.append(min_str)
    return result


string_of_numbers = string_int(insert_number())
max_str = str(Maximum(string_of_numbers))
min_str = str(Minimum(string_of_numbers))
print(''.join(Create_Row(max_str, min_str)))