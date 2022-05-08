# Найти НОК двух чисел


def insert_number():
    '''Function for inserting number. Don't have argument, and returns inserting integer number'''
    return input('Insert number: ')


def check_int(number):
    '''Function for checking inserted number. It accepts value, and if it's int it will be return, else this function will be called again.'''
    try:
        return int(number)
    except:
        print("Illegal number. Try one more time")
        return check_int(insert_number())


def nod(x1, x2):
    '''Function that definite NOD of two numbers. It has two integer arguments. And returns NOD'''
    if x2 == 0:
        return x1
    else:
        return nod(x2, x1%x2)


def nok(x1, x2):
    '''This function definites NOK of two numbers. It has two integer arguments and returns NOK - integer number'''
    return x1*x2//nod(x1,x2)


print(nok(check_int(insert_number()), check_int(insert_number()))) # there is calling all functions