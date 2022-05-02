# Найти сумму чисел списка стоящих на нечетной позиции

def insert_user():
    '''Function is for inserting string. Also here program is checking type of inserted elem. Function return list of string numbers'''
    correct = False
    while correct == False:
        for_checking = 0
        line = list(input('Insert your line of numbers').split(' '))
        for i in range(0, len(line)):
            if line[i].isdigit():
                correct = True
            else:
                print(f'{line[i]} is not integer')
                for_checking += 1
        if for_checking > 0:
            correct = False
            print('Incorrect inserted string. Try again!')
    return line

def from_string_to_int(list):
    '''Function take argument from function 'insert_user()' and retype each item. And return result like list of integer numbers'''
    for i in range(0, len(list)):
        list[i] = int(list[i])
    print(list)
    return list


def count_sum_of_odd_numbers(list):
    '''Function is receiving list of integer numbers, execute sum of odd elements and return result'''
    result = 0
    for i in range(1, len(list), 2):
        result += list[i]
    return result

print(count_sum_of_odd_numbers(from_string_to_int(insert_user())))