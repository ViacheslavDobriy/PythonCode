# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]

def create_line(N):
    '''Function will get user's number and will return list with results of multiples of numbers from 1 to user's number'''
    if N > 0:
        result_list = [1]
        if N != 1:
            for i in range(2, N+1):
                result_list.append(result_list[i-2]*i)
    else:
        result_list = [0]
    return result_list

def checking_legal(N_number):
    '''This function will check correct or incorrect user's number'''
    checking_result = True
    if N_number < 0:
        checking_result = False
        print('You inserted illegal number!')
    return checking_result

user_number = int(input('Insert your number:'))
result_checking = checking_legal(user_number)
if result_checking:
    print(create_line(user_number))