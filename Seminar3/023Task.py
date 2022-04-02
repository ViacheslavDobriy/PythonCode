# Найти произведение пар чисел в списке. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 

import math
list = [2, 3, 4, 5, 6, 7, 8, 10, 11]
res_list = []
len_res_list = math.ceil(len(list)/2)
temp = 0

for i, x in enumerate(list):
    if len(res_list) != len_res_list:
        temp = list[i] * list[-1-i]
        res_list.append(temp)
        
print(res_list)
        