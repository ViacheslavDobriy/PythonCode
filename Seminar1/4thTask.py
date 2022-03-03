# Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30

number = int(input('Enter number'))

divisors = [5,10,15,30]
if number%divisors[0]==0 and number%divisors[1]==0 or number%divisors[2]==0 and number%divisors[3]!=0:
    print('True')
else:
    print('False')
