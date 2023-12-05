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

    cards = get_cards()
    total = 0

    for card in cards:
        
        points = 0

        win, game = card
        overlap = len(win+game) - len(set(win+game))

        if overlap != 0:
            points = 2**(overlap-1)

        total += points

    return total

def get_scratch():

    cards = get_cards()
    nums = [1] * len(cards)

    for n, card in enumerate(cards):

        copies = nums[n]
        
        win, game = card
        overlap = len(win+game) - len(set(win+game))

        for c in range(n+1, n+overlap+1):
            nums[c] += copies

    return sum(nums)

print('Part 1:', get_points())
print('Part 2:', get_scratch())