# Реализовать алгоритм перемешивания списка.
import random
def input_line():
    user_line = list(input('Insert what do you want see in this list.').split(' '))
    while '' in user_line:
        user_line.remove('')
    return user_line

def shake_line(inserted):
    shaked_line = []
    for each in range(0, len(inserted)):
        k = random.randint(0, len(inserted)-1)
        while inserted[k] in shaked_line or k == each:
            k = random.randint(0, len(inserted)-1)
        shaked_line.append(inserted[k])
    return shaked_line

print(shake_line(input_line()))