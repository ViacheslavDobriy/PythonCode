# Строка содержит набор чисел. Показать большее и меньшее число
# Символ-разделитель - пробел

string_of_numbers = [14,543,123,63,2,76,-123,0,12,67,345,2345,-432]

def Maximum(string_of_numbers):
    max = string_of_numbers[0]
    for i in range(0,len(string_of_numbers)):
        if string_of_numbers[i] > max:
            max = string_of_numbers[i]
    return max

def Minimum(string_of_numbers):
    min = string_of_numbers[0]
    for i in range(0,len(string_of_numbers)):
        if string_of_numbers[i] < min:
            min = string_of_numbers[i]
    return min

max_str = str(Maximum(string_of_numbers))
min_str = str(Minimum(string_of_numbers))

def Create_Row(max_str, min_str):
    result = []
    result.append(max_str)
    result.append(' ')
    result.append(min_str)
    return result
    
print(''.join(Create_Row(max_str, min_str)))