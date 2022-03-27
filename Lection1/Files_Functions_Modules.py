##### WORK WITH FILES #####
# a - open for adding data
# r - open for reading data
# w - open for writing data
# w+, r+
#######Examples#######
###########1########## WRITING №1

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# data.write('\nLINE 12\n')
# data.write('LINE 13')
# data.close()

###########2########## WRITING №2

# with open('file.txt', 'w') as data:
#     data.write('line1\n')
#     data.write('line2\n')

###########3########## READING

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()

##### WORK WITH FUNCTION AND MODULES #####

# import hello as h
# NEED TO WORK ON IT. PYTHON DON'T SEE FILE hello
# print(h.f(1))

#######Examples#######
###########1########## 

# def new_string(symbol, count = 3):
#     return symbol*count

# print(new_string('!', 6))
# print(new_string('!'))
# print(new_string(4))

###########2##########

# def concatenatio(*params):
#     res: int = 0
#     for item in params:
#         res += item
#     return res

# print(concatenatio('a', 's', 'd', 'w')) # asdw
# print(concatenatio('a', '1')) # a1d2
# print(concatenatio(1, 2, 3, 4)) # TypeError: ...

##### RECURSION #####

# def fib(n):
#     if n in [1,2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# list = []
# for e in range(1,10):
#     list.append(fib(e))
#     print(list) # 1 1 2 3 5 8 13 21 34

##### KORTEZH ##### - это некий неизменямый список

# t = ()
# print(type(t))           # tuple
# t = (28, 9, 1990)
# print(type(t))           # tuple
# (a) = (3, 4)
# print(a)
# print(a[-1])
# a[0] = 12
# a = (2,3,4)

# for item in a:
#     print(item)
    
##### DICTIONARY #####

# dictionary = {}
# dictionary = \
#     {
#         'up': '!',
#         'left': '<-',
#         'down': '||',
#         'right': '->'
#     }
# print(dictionary) 
# print(dictionary['left'])
# # типы ключей могут отличаться

# print(dictionary['up']) # !
# del dictionary['left'] # delete item
# for item in dictionary:
#     print('{}: {}'.format(item, dictionary[item]))

# for k in dictionary.keys():
#     print(k)

# for k in dictionary.values():
#     print(k)

# for k in dictionary:
#     print(k)

##### SETS #####

# colors = {'red', 'green', 'blue'}
# print(colors)
# colors.add('red')
# print(colors)
# colors.add('gray')
# print(colors)
# colors.remove('red')
# print(colors)
# colors.discard('red')
# print(colors)
# colors.clear()
# print(colors)

# a = {1,2,3,5,8}
# b = {2,5,8,13,21}
# # c = a.copy()        
# # u = a.union(b)
# # i = a.intersection(b)
# # dl = a.difference(b)
# # dr = b.difference(a)
# # print(a)
# # print(b)
# # print(c)
# # print(u)
# # print(i)
# # print(dl)
# # print(dr)

# q = a \
#     .union(b) \
#     .difference(a.intersection(b))
# print(q)

# s = frozenset(a)

##### LISTS #####

# list1 = [1,2,3,4,5]
# list2 = list1

# for e in list1:
#     print(e)

# print()

# for e in list2:
#     print(e)

# list2[4] = 222

# for e in list1:
#     print(e)

# print()

# for e in list2:
#     print(e)

# print(len(list1))
# print(list1.pop(3))
# print(list1)

# print(list1.insert(3,11))
# print(list1)

# print(list1.append(11))
# print(list1)