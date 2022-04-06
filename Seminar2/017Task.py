# Задать список из N элементов, заполненных числами из [-N, N].
# Найти произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

import random

def Random_range(number):
    '''Generate new list with N numbers. It can have numbers from range [-user_numbers, user_numbers]'''
    list = []
    for i in range(userNumber):
        list.append(random.randrange(-userNumber, userNumber))
    print(list)
    return list

def Take_index():
    '''Function take indexes from file and save elements in the new list'''
    index_row = []
    with open('C:/Users/user/Desktop/GeekBrains/Python/Seminar2/file.txt', 'r') as data: 
        for line in data:
            index_row.append(int(line))
    return index_row

def Multiply(first, second):
    '''Function returns result of multipliing all elements with indexes from file'''
    result = 1
    for i in second:
        result *= first[i]
    return result

userNumber = int(input('Input any number.'))
print(Multiply(Random_range(userNumber), Take_index()))