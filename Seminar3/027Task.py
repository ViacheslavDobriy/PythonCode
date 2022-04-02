# Строка содержит набор чисел. Показать большее и меньшее число
# Символ-разделитель - пробел

# string_of_numbers = []

user_number = str(input('Insert numbers'))

def string_int(user_number):
    return [int(x) for x in user_number.split(' ')]
string_list = string_int(user_number)
print(string_list)
min=min(string_list)
max=max(string_list)
print(f'{max} {min}')
# def Maximum(string):
#     max = string_of_numbers[0]
#     for i in range(0,len(string_of_numbers)):
#         if string_of_numbers[i] > max:
#             max = string_of_numbers[i]
#     return max

# def Minimum(string_of_numbers):
#     min = string_of_numbers[0]
#     for i in range(0,len(string_of_numbers)):
#         if string_of_numbers[i] < min:
#             min = string_of_numbers[i]
#     return min

# max_str = str(Maximum(string_of_numbers))
# min_str = str(Minimum(string_of_numbers))

# def Create_Row(max_str, min_str):
#     result = []
#     result.append(max_str)
#     result.append(' ')
#     result.append(min_str)
#     return result
    
# print(''.join(Create_Row(max_str, min_str)))