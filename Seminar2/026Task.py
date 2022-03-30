# Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов. 

n = 4
def fib(n):
    if n in [1,2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)

list = []
for e in range(1,10):
    list.append(fib(e))
    print(list) # 1 1 2 3 5 8 13 21 34