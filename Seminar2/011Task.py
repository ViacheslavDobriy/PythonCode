# Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

length = int(input('How many numbers you want to see?'))
i = 1
if length > 0:
    list = [1]
    while i < length:
        list.append(list[i-1]*(-3))
        i = i + 1
    print(list)
else: 
    print("Don't you want to see my list? It's a pity..")

