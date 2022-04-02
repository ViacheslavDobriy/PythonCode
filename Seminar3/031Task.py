# Составить список простых множителей натурального числа N
# 36 = 2*2*3*3
number = int(input('Insert number'))

list = []

for i in range(2,number):
    while number %i == 0:
        number/= i
        list.append(i)
print(list)

# import math 

# num = int(input('Введите число: ')) 
# def faktorizaciya(num): 
     
#     while num % 2 == 0: 
#         print(2) 
#         num = num / 2 
 
#     for i in range(3, int(math.sqrt(num)) + 1, 2): 
 
#         while num % i == 0: 
#             print(i) 
#             num = num / i 
#     if num > 2: 
#         print(num)   
# faktorizaciya(num)
