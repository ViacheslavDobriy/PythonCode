# Подсчитать сумму цифр в вещественном числе.

def sum_of_digits(number):
    '''Counting sum of all digits from the list'''
    sum = 0
    for i in number:
        while i >= 1:
            sum+= i%10
            i = int(i/10)
    return sum

def is_it_negative(number):
    '''I'm checking that first number of user' number is positive. If it's not positive i will do that'''
    if number[0] < 0:
        number[0] *= -1
    return number

user_number = list(map(int, input('Insert float number').split('.')))

user_number = is_it_negative(user_number)
print(user_number)
print(f'{sum_of_digits(user_number)} - is sum of digits')