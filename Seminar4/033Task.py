# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k. 
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random
k = 0
while k == 0:
    k = int(input('Insert k'))
    if k == 0:
        print('Illegal value')

list_rates = []

for i in range(1,k+1):
    rate = random.randrange(0,101)
    list_rates.append(rate)

with open('C:\Users\user\Desktop\GeekBrains\Python\Seminar4', 'w') as data:
    for i in range(1, len(list_rates)+1):
        if list_rates[i] !=0:
            data.write('+ {list_rates[-i]}*x^{i} ')
    
    # data.write('{}\n')
    # data.write('line2\n')

