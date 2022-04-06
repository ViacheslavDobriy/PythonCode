# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k. 
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

def Create_line(line1):
    '''I do polynomial here'''
    result_line = []
    constant_string = ''.join('*x^')
    for i in range(0, len(line1)):
        if line1[i] != 0 and i != len(line1) - 1:
            result_line.append(f'{line1[i]}{constant_string}{len(line1) - i - 1} + ')
        elif i == len(line1) - 1:
            if line1[i] != 0:
                result_line.append(f'{line1[i]} = 0')
            else:
                result_line.pop(len(result_line) - 1)
                result_line.pop(len(result_line) - 2)
                result_line.append('= 0')
    result_line = ''.join(result_line)
    return result_line

def Input_and_Correct():
    '''Inviting to insert index of polynomial and check correct'''
    x = 0
    while x == 0:
        x = int(input('Insert x'))
        if x == 0:
            print('Illegal value')
    return x

def Random_rates(number):
    '''Build list with random rates'''
    list_rates = [0]
    while list_rates[0] == 0:
        list_rates = []
        for i in range(1,number+2):
            rate = random.randrange(0,101)
            list_rates.append(rate)
    return list_rates

def Put_in_file(str):
    '''Put whole string to the file'''
    with open('C:/Users/user/Desktop/GeekBrains/Python/Seminar4/file_for_033.txt', 'w') as data:
        data.writelines(str)

user_number = Input_and_Correct()
Put_in_file(Create_line(Random_rates(user_number)))