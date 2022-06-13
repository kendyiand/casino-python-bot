import random
from lib import *

def get_roll():
    rnd = random.randint(0,36)
    if rnd in red:
        return [rnd, 'red']
    if rnd in black:
        return [rnd, 'black']
    if rnd in green:
        return [rnd, 'green']    
        

def process(bet_number, bet_color):
    rolled = get_roll()
    
    if colors_dict[bet_color] == rolled[1]:
        m = multiplayer[colors_dict[bet_color]]
        return f'{rolled[0]} {rolled[1]} dropped\nYou won ${bet_number * m}'
    else:
        return f'{rolled[0]} {rolled[1]} dropped\nYou lost ${bet_number}'
