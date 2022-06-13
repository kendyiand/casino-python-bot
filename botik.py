import telebot
import time
from lib import *
from functions import *

@bot.message_handler(commands=['start'])
def start_msg(message):
    bot.send_message(message.chat.id, 'Choose color', reply_markup=color)
    
@bot.message_handler(content_types='text')
def make_bet(message):
    if message.text in ['Red 🟥','Black ⬛','Green 🟩']:
        bot.send_message(message.chat.id, 'Place your bet', reply_markup=telebot.types.ReplyKeyboardRemove())
        bet_color = message.text
        bot.register_next_step_handler_by_chat_id(message.chat.id, roll, bet_color)

def roll(message, bet_color):
    try:
        bet_number = int(message.text)
        result = process(bet_number, bet_color)

        bot.send_message(message.chat.id, f'Your betAAA is {bet_number}$ on {bet_color}')
        time.sleep(0.5)
        edit_msg = bot.send_message(message.chat.id, 'Rolling')
        time.sleep(0.2)
        bot.edit_message_text(rolling1, message.chat.id, edit_msg.message_id)
        time.sleep(0.2)
        bot.edit_message_text(rolling2, message.chat.id, edit_msg.message_id)
        time.sleep(0.2)
        bot.edit_message_text(rolling3, message.chat.id, edit_msg.message_id)
        time.sleep(0.2)
        bot.edit_message_text(result, message.chat.id, edit_msg.message_id)
        bot.register_next_step_handler_by_chat_id(message.chat.id, callback=make_bet)

    except Exception as err:
        print(err)
        bot.send_message(message.chat.id, 'Write number')
        bot.register_next_step_handler_by_chat_id(message.chat.id, callback=roll)


bot.polling(none_stop=True, interval=0)