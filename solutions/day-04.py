from _getinput import *
import regex as re

# --- Day 4: Scratchcards ---

def get_cards():

    input = getinput(day = '04', example=True)

    for i, line in enumerate(input):

        card, game = line.split('|')
        card, win = card.split(':')

        win = re.findall(r'\d+', win)
        game = re.findall(r'\d+', game)

        input[i] = [win, game]
    
    return input

def get_points():

    total = 0
    
    cards = get_cards()

    for card in cards:
        
        points = 0

        win, game = card
        n_overlap = len(win+game) - len(set(win+game))

        if n_overlap != 0:
            points = 2**(n_overlap-1)

        total += points

    return total

print('Part 1:', get_points())
