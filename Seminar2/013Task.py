# Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

from tokenize import Number


def Number_Of_Occurrences(str1, str2):
    result = 0
    for x in range(0, len(str1)):
        for y in range(0, len(str2)):
            if str1[x] == str2[y]:
                result += 1
    return result

user_string1 = list(input('Insert 1st string').split())
user_string2 = list(input('Insert 2nd string').split())

print(user_string1)
print(user_string2)

print(f'{Number_Of_Occurrences(user_string1, user_string2)} times first string have the same words like in second string')
# list(map(int, input('Insert 1st string')))


                