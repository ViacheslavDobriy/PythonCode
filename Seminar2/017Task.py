# Задать список из N элементов, заполненных числами из [-N, N].
# Найти произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

userNumber = int(input('Input any number.'))
list = []
i = 0
for i in range(-userNumber, userNumber+1):
    list.append(i)
result = 1
with open('C:/Users/user/Desktop/GeekBrains/Python/Seminar2/file.txt', 'r') as data: 
    for line in data:
        temple = int(line)
        result*= list[temple]
print(list)
print(result)



