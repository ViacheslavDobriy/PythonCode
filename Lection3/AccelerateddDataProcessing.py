######## lambda, filter, map, zip, enumerate, List Comprehension 
######## ANONIM 'LAMBDA' FUNCTION #########
############## FIRST EXAMPLE ##############
###########################################

# def sum(x):
#     return x+10

# def mult(x):
#     return x**2

# def math(operation, value):
#     print(operation(value))

# math(mult, 3)
# math(sum, 18)

######## SECOND EXAMPLE ########
################################

# def sum(x, y):
#     return x+y

# f = lambda q, w: q+w + 9

# def mult(x, y):
#     return x*y

# def calc(op, a, b):
#     print(op(a,b))
#     return op(a,b)

# calc(lambda q, w: q+w + 9, 4, 5)
# calc(lambda x, y: x*y -8, 4, 5)

# def f(x):
#     return x**2

# g = f
# print(type(f))
# print(type(g))

# print(f(2))
# print(g(2))

########### LIST COMPREHENSION ############
############## FIRST EXAMPLE ##############
###########################################

# list = []

# for i in range(1, 101):
#     # if(i%2) ==0:
#     list.append(i)

# print(list)

# list = [(i, f(i)) for i in range(1, 21) if i%2 == 0]
# print(list)

############### MY SOLUTION ###############
###########################################

# def f(x):
#     return x**2

# list = []

# path = 'C:/Users/user/Desktop/GeekBrains/Python/Lection3/list.txt'
# data = open(path, 'r')
# for list in data:
#     print(list)
# data.close()
# print(list)
# new_list = [int(x) for x in list.split(' ') if x.isdigit()]
# print(new_list)
# new_list = [(i, f(i)) for i in new_list if i%2 == 0]
# print(new_list)

############ SERGEY'S SOLUTION ############
###########################################

# def select(f, col):     #--------> instead of map
#     return [f(x) for x in col]

# def where(f, col):      #--------> instead of filter
#     return [x for x in col if f(x)]

# data = '1 2 5 6 9 12 67'.split()

# res = map(int, data)
# res = filter(lambda x: not x%2, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)

################### MAP ###################
###########################################

# li = [i for i in range(1, 21)]
# print(li)
# li = list(map(lambda x: x+10, li))
# print(li)

# data = list(map(int, '1 2 4 6 34'.split()))
# for e in data:
#     print(e+10)
# print('---')
# for e in data:
#     print(e+10)

################# FILTER ##################
###########################################

# data = [x for x in range(1, 10)]

# res = list(filter(lambda x: not x%2, data))
# print(res)

################## ZIP ####################
###########################################

# users = ['user1', 'user2', 'user3', 'user4', 'user5', 'user6']
# ios = [4, 3, 9, 11, 5, 89]
# salary = [111,222,333]
# data = list(zip(users, ios, salary))
# print(data)

############### ENUMERATE #################
###########################################

# users = ['user1', 'user2', 'user3', 'user4', 'user5', 'user6']
# ios = [4, 3, 9, 11, 5, 89]
# salary = [111,222,333]
# data = list(enumerate(users))
# print(data)