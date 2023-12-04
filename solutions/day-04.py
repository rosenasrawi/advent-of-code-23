from _getinput import *
import regex as re

# --- Day 4: Scratchcards ---

def get_cards():

    input = getinput(day = '04', example=False)

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
        win, game = card

        points = 0

        for g in game:
            if g in win:
                if points == 0: 
                    points +=1
                else: 
                    points*=2

        total += points

    return total

print('Part 1:', get_points())