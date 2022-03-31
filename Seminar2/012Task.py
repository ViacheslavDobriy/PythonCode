# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

userNumber = int(input('How many numbers do you wanna see?'))
dictionary_index_value = []
for i in range(1,userNumber+1):
    dictionary_index_value.append(3 * i + 1)
# print(dictionary_index_value)
