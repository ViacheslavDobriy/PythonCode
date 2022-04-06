# Задать список из n чисел последовательности (1+1/n)^n и вывести на экран их сумму

def Create_List_Positive_N(n):
    '''Create list of sequence if user's number is pozitive'''
    list_of_sequence = []
    for i in range(1, n+1):
        list_of_sequence.append(round((1+1/i)**i, 3))
    return list_of_sequence

def Sum_of_sequence(list):
    result = 0
    for i in list:
        result += i
    return result

def Create_List_Negative_N(n):
    '''Create list of sequence if user's number is negative'''
    list_of_sequence = []
    for i in range(-2, n-1, -1):
        list_of_sequence.append(round((1+1/i)**i, 3))
    return list_of_sequence

user_number = int(input('Insert integer number: '))

if user_number == 0 or user_number == -1:
    while user_number == 0 or user_number == -1:
        print("Insert Correct integer number! Your number can't to be 0 or -1")
        user_number = int(input('Insert integer number: '))
if user_number >= 1:
    print(Sum_of_sequence(Create_List_Positive_N(user_number)))
else:
    print(Sum_of_sequence(Create_List_Negative_N(user_number)))
    
