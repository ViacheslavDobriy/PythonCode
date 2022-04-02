##### ТИПЫ ДАННЫХ И ПЕРЕМЕННЫЕ #####
# INT, FLOAT, BOOLEAN, STR, LIST, NONE

# value = None
# # print(type(value))
# a = 123
# b = 1.23
# # print(type(a))
# # print(type(b))
# value = 1234
# # print(type(value))
# s = 'qwerty'

# f = False
# print(f)

# list = ['1','2','3', 1,2,3,4.5, True]
# col = ['hello', 1.2, 4.5, True]
# print(list)
# print(col)

##### PRINT #####

# print(s) # вывод строки
# print(a,'-',b,'-',s)                     # Интерполяция строк
# print(f'{a} - {b} - {s} ')               # Интерполяция строк
# print('{0} - {1} - {2}'.format(a,b,s))   # Интерполяция строк

##### ВЫВОД И ВВОД ДАННЫХ #####
# print() # вывод данных
# input() # ввод данных

# print('Input a')
# a = int(input())
# print('Input b')
# b = int(input())
# print(a,'+', b, '=', a+b)

##### АРИФМЕТИЧЕСКИЕ ОПЕРАЦИИ #####
# ** - возведение в степень
# // - деление на цело
# % - остаток от деления

# a = 1.3
# b = 3
# c = round(a * b,5)
# print(c)

# a = 3
# a += 5

# print(a)

##### ЛОГИЧЕСКИЕ ОПЕРАЦИИ #####

# a = 1 < 4
# print(a)

# a = 1 < 3 < 5
# print(a)

# f = 1 > 2 or 4 < 6
# print(f)

# f = [1,2,3,4]
# print(f)
# print(not 0 in f)

# is_odd = not f[0] % 2
# print(is_odd)

##### УПРАВЛЯЮЩИЕ КОНСТРУКЦИИ #####
############### IF ################

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# username = input('Input name: ')
# if username == 'Маша':
#     print('Hooray! This is MASHA!')
# elif username == 'Марина':
#     print('I am so hungry!')
# elif username == 'Slava':
#     print('Slava - Top')
# else:
#     print('Hello, ', username)

############### WHILE ################

# original = 279
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)

############### WHILE-ELSE ################

# original = 9173
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print('So')
#     print('Stop')
# print(inverted)

############### FOR ################

# list = [1,2,3,4,10,5]
# for i in list:
#     print(i)

# r = range(1,5, 2)
# for i in r:
#     print(i)

############### WORK WITH STRING ################

# text = 'eat even more those soft french pies'
# print(len(text))                                # number of symbols
# print('even' in text)                           # checking word or frase
# print(text.isdigit())                           # checking digit
# print(text.islower())                           # checking lower all symbols or no
# print(text.replace('even', 'EVEN'))             # priint string and put instead of first value second value

# for c in text:
#     print(c)

############### СРЕЗЫ В СТРОКЕ ################

# text = 'eat even more those soft french pies'
# print(text[0])
# print(text[1])
# print(text[len(text) - 1])
# print(text[-4])
# print(text[:])
# print(text[:])
# print(text[len(text)-2:])
# print(text[2:9])
# print(text[2:-15])
# print(text[0:len(text):6])
# print(text[::6])
# text = text[2:9] + text[-5] + text[-2]

############### MORE LIST ################

# numbers = [1,2,3,4,5]
# print(numbers)
# ran = range(1,6)
# print(type(ran))
# numbers = list(ran)
# print(type(numbers))

############### FUNCTION ################

# def f(x):
#     if x == 1:
#         return 'INT'
#     elif x == 2.3:
#         return 23
#     else:
#         return

# arg = None
# print(f(arg))
# print(type(f(arg)))

import os
print(os.getcwd())
import hello

print(hello.x(2))