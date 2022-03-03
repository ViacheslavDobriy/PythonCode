# Вывести на экран числа от -N до N

print('Введите число')
usernumber = int(input())
count = -usernumber
while(count<=usernumber):
    print('{0} '.format(count))
    count = count + 1

