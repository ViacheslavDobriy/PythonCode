# Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её.

import random

def Who_is_first(choice):
    generated_number = random.randint(0, 1)
    print(generated_number)
    turn = 0
    if choice == generated_number:
        turn += 1
    else:
        turn += 2
    return turn

def print_field():
    print('____|____|____')
    print('____|____|____')
    print('    |    |    ')

def where_you_can_step():
    print('__1_|__2_|__3_')
    print('__4_|__5_|__6_')
    print('  7 |  8 |  9 ')
player1_name = input("Welcome to the game! Insert player's №1 name: ")
player2_name = input("Welcome to the game! Insert player's №2 name: ")

player1_choice = int(input('Player №1 insert your digit from 0 till 1, if your number and my generated number are the same - your turn, else second player will be first'))

print_field()
where_you_can_step()
# if Who_is_first(player1_choice) == 1:
# Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования.
