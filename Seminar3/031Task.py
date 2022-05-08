# Составить список простых множителей натурального числа N
# 36 = 2*2*3*3


def inserting_number():
    '''Function is inviting user to insert number. It returns inserted string'''
    return input('Insert number')


def check_int(number):
    '''Function for checking inserted number. It accepts value, and if it's int it will be return, else this function will be called again.'''
    try:
        return int(number)
    except:
        print("Illegal number. Try one more time")
        return check_int(inserting_number())


def prime_factors(number):
    '''Function make list of simple factors. It has integer argument and returns list'''
    factors_list = []
    for i in range(2, number):
        while number % i == 0:
            number /= i
            factors_list.append(i)
    return factors_list


print(prime_factors(check_int(inserting_number())))
