# Вывести квадрат числа

def square_of_number():
    print('Input your number')
    userNumber = int(input())
    print(f'Square of {userNumber} is - ')
    return userNumber*userNumber

print(square_of_number())