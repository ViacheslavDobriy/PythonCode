# Найти максимальное из пяти чисел

from random import randint


number1 = randint(1,101)
number2 = randint(1,101)
number3 = randint(1,101)
number4 = randint(1,101)
number5 = randint(1,101)

list = [number1, number2, number3, number4, number5]

max = number1
count = 0
while(count < 5):
    print(list[count])
    if(max<list[count]):
        max = list[count]
    count = count + 1
print('{} - the biggest number from your row'.format(max))