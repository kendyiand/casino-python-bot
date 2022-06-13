
from telebot import types
import telebot

TOKEN = '5531782962:AAGOah0gIbINkzC7Ri3GLmXfLhHGAv39EZs'
bot = telebot.TeleBot(TOKEN)

color = types.ReplyKeyboardMarkup(resize_keyboard=True)
color.row('Red 🟥')
color.row('Black ⬛')
color.row('Green 🟩')


red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
green = [0]

rolling1 = 'Rolling.' 
rolling2 = 'Rolling..'
rolling3 = 'Rolling...'

colors_dict = {
    'Red 🟥': 'red',  
    'Black ⬛': 'black', 
    'Green 🟩': 'green'
    }

multiplayer = {
    'red': 2,
    'black': 2,
    'green': 35,
}
