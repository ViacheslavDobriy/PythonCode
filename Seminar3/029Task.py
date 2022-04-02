# Найти НОК двух чисел

user_number1 = int(input('Insert number 1'))
user_number2 = int(input('Insert number 2'))

def nod(x1, x2):
    if x2 == 0:
        return x1
    else:
        return nod(x2, x1%x2)
print(nod(user_number1, user_number2))
def nok(x1, x2):
    return x1*x2//nod(x1,x2)
print(nok(user_number1, user_number2))