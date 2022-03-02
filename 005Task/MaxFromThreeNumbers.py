# Найти максимальное из трех чисел 

number1 = int(input('Enter first number'))
number2 = int(input('Enter second number'))
number3 = int(input('Enter third number'))

array = [number1, number2, number3]
max = array[0]
count = 0
while(count < 3):
    if(max<array[count]):
        max = array[count]
    count = count + 1
print('{} - the biggest number from your row'.format(max))