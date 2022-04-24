from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
import random

updater = Updater('5352372609:AAEk1VYI9_G-2-q57PYGlTP7RUN0mO4wq4A')

board = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


def help_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'/hi\n/help\n/start')


def start_game_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'Начало игры!')


def draw_board(update: Update, context: CallbackContext):
    global board
    update.message.reply_text(
        f'{board[0]}|{board[1]}|{board[2]}\n{board[3]}|{board[4]}|{board[5]}\n{board[6]}|{board[7]}|{board[8]}')
    update.message.reply_text('Do your turn')


def redraw_board(update: Update, context: CallbackContext, choice, who_do_step):
    global board
    if who_do_step == 'Player':
        for i in range(0, len(board)):
            if board[i] == choice:
                board[i] = 'X'
        update.message.reply_text(
            f'{board[0]}|{board[1]}|{board[2]}\n{board[3]}|{board[4]}|{board[5]}\n{board[6]}|{board[7]}|{board[8]}')
    else:
        for i in range(0, len(board)):
            if board[i] == choice + 1:
                board[i] = '0'
        update.message.reply_text(
            f'{board[0]}|{board[1]}|{board[2]}\n{board[3]}|{board[4]}|{board[5]}\n{board[6]}|{board[7]}|{board[8]}')


def turn_number():
    global board
    step = 0
    for each in range(0, len(board)):
        if board[each] == 'X':
            step += 2
    return step


def NPC_no_lose_next_turn():
    global board
    win_lines = [[board[0], board[1], board[2]],
                 [board[3], board[4], board[5]],
                 [board[6], board[7], board[8]],
                 [board[0], board[3], board[6]],
                 [board[1], board[4], board[7]],
                 [board[2], board[5], board[8]],
                 [board[0], board[4], board[8]],
                 [board[2], board[4], board[6]]]
    for i in range(0, 8):
        current_line = 0
        for k in range(0, 3):
            if win_lines[i][k] == 'X':
                current_line += 1
                if current_line == 2:
                    for each in win_lines[i]:
                        if each != 'X':
                            if type(each) == type(9):
                                return each - 1
# Нужно добавить функцию, которая пробует победить игрока еслли не находит ряд с двумя Х в ряд.

# print(NPC_no_lose_second_turn())
def NPC_no_lose_first_turn():
    global board
    if board[4] == 'X':
        no_lose_list = [0, 2, 6, 8]
        return random.choice(no_lose_list)
    else:
        return 4


def NPC_turn(update: Update, context: CallbackContext, step):
    global board
    who_do_turn = 'NPC'
    if step == 2:
        update.message.reply_text('I do my first turn')
        redraw_board(update, context, NPC_no_lose_first_turn(), who_do_turn)
    if step == 4 or step == 6:
        print('I do my best')
        redraw_board(update, context, NPC_no_lose_next_turn(), who_do_turn)


def Player_turn(update: Update, context: CallbackContext):
    user_turn = update.message.text
    turn = int(user_turn)
    return turn


def round(update: Update, context: CallbackContext):
    who_do_turn = 'Player'
    redraw_board(update, context, Player_turn(update, context), who_do_turn)
    NPC_turn(update, context, turn_number())


# def who_is_first(update: Update, context: CallbackContext):
#     draw = False
#     while not draw:
#         hidden_number = random.randint(0, 10)
#         update.message.reply_text(f'Я выберу цифру от нуля до 9. Введите цифру от 0 до 9. Если вы будете ближе, чем NPC, к моей цифре - ваша очередь будет первой!')
#         user_choice = update.message.text
#         user_choice = int(user_choice)
#         npc_choice = random.randint(0, 10)
#         if abs(hidden_number - user_choice) == abs(hidden_number - npc_choice):
#             update.message.reply_text(f"Я выбрал: {hidden_number}. Ты взял: {user_choice}, но NPC взял: {npc_choice}. Это означает ничью, ещё раз!")
#         elif abs(hidden_number - user_choice) > abs(hidden_number - npc_choice):
#             update.message.reply_text(f"Я выбрал: {hidden_number}. Ты взял: {user_choice}, но NPC взял {npc_choice}. NPC ходит первым!")
#             draw = True
#             return 'NPC'
#         else:
#             print(f"Я выбрал: {hidden_number}. Ты взял: {user_choice}, но NPC взял {npc_choice}. Ты ходишь первым! ")
#             draw = True
#             return 'Player'

# updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('game', draw_board))
updater.dispatcher.add_handler(MessageHandler(Filters.text, round))
print('Server is working')
updater.start_polling()
updater.idle()
