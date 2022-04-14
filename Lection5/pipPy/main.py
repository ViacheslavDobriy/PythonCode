from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bot_commands import *
updater = Updater('5352372609:AAEk1VYI9_G-2-q57PYGlTP7RUN0mO4wq4A')

updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('sum', sum_command))

print('Server is working!')
updater.start_polling()
updater.idle()


# import emoji
# from isOdd import isOdd
# print(emoji.emojize('Python is :thumbs_up:'))

# print(isOdd(1))