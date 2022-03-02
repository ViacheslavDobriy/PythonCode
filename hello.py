from os import remove


value = None
print (type(value))
a = 123
b = 1.23
print (type(a))
print (type(b))
value = 12334
print (type(value))
s = 'Hello "world'

print(s) # вывод строки
print(a, '-',b, '-',s)
print('{1} - {2} - {0}'.format(a,b,s))
print(f'{a} - {b} - {s}')

list = ['1', '2', '3', 'hello', 1, 2, 3.45, True]
print(list)

func = 1
T = 4
x = 123

print(func<T>(x))

f = 1 > 2 or 4 < 6

#print(not 2 in f)

#is_odd = f[0] % 2 == 0
#print(is_odd)

# Управляющие конструкции
# if, if-else

# Управляющие конструкции
# while

# Управляющие конструкции
# while-else

# Управляющие конструкции
# for

for i in 'qwerty':
    print(i)

# ecsr

text = 'съешь еще этих мягких французских булок'
print(text[0])
print(text[2:5])

# Списки: введение
## list = list

numbers = [1,2,3,4,5]
print(numbers)
ran = range(1,5)
print(type(ran))
#colors = ['red', 'yellow', 'green']
#colors.remove
#append

# Функции

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 'Integer'
