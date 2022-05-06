# Написать программу преобразования десятичного числа в двоичное

number = 14


def binary_func(number):
    '''Function take int number and make binary number of it. It returns list that consists from 0 and 1'''
    binary_number = []
    while number >= 1:
        binary_digit = number % 2
        number = number // 2
        binary_number.append(str(binary_digit))
    return binary_number


def reverse_list(list_of_0_and_1):
    '''Function take list of 0 and 1 and return inverted list'''
    list_of_0_and_1.reverse()
    return ''.join(list_of_0_and_1)


print(f'{number} in binary is {reverse_list(binary_func(number))}')