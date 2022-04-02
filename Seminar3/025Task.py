# Написать программу преобразования десятичного числа в двоичное

number = 14

def binary_func(number):
    binary_number = []
    while number >= 1:
        binary_digit = number%2
        number = number // 2
        binary_number.append(str(binary_digit))
    return binary_number
result = binary_func(number)
print(result)
result.reverse()
print(result)
print(''.join(result))


# i = 1
# while i <= -len(binary_number):
#     new_line.append(binary_number[-i])
#     i = i - 1
# print(new_line)