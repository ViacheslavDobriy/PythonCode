# Показать первую цифру дробной части числа

print('Enter number')

n = float(input())

result = int(n*10 % 10)

print(result)