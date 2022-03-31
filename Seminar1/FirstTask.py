# Найти максимальное из пяти чисел

from random import randint

list = []

for i in range(0,5):
    list.append(randint(1,101))

max = list[0]
count = 0
while(count < 5):
    print(list[count])
    if(max<list[count]):
        max = list[count]
    count = count + 1
print('{} - the biggest number from your row'.format(max))