# Даны два числа. Показать большее и меньшее число

print('Input first number')
number1 = int(input())
print('Input second number')
number2 = int(input())
if(number1>number2):
    print('First number ({}) is bigger than second number ({})'.format(number1,number2))
elif(number1<number2):
    print('Second number ({1}) is bigger than first number ({0})'.format(number1,number2))
else:
    print('These two numbers are equals to each other')