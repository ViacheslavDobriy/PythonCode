# Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

list2 = [1, 2, 3, 5, 1, 5, 3, 10]

number = list(set(list2))
print(number)
# list1 = list(number)
# print(list1)
# result_list = []
# digit = list1[0]
# for i in list1:
#     result_list.append(digit)

# my_list = [1, 2, 3, 5, 1, 5, 3, 10]
# my_set = set(my_list)
# print(my_set)
# my_list2 = list(my_set)
# print(my_list2)

