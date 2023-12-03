from _getinput import *
import regex as re

# --- Day 2: Cube Conundrum ---

bag = {
    'red': 12,
    'green': 13,
    'blue': 14
}

games = getinput('02', example=False)

totalIDs = 0

for g in games:

    game, picks = g.split(':')

    game = int(re.sub('\D', '', game))

    picks = re.sub(',', '', picks).split(';')
    picks = [pick.split() for pick in picks]

    for pick in picks:
        while len(pick) >= 2:
            num = pick.pop(0)
            col = pick.pop(0)

            possible = bag[col] >= int(num)

            if not possible:
                break
        
        if not possible:
            break

    if possible: 
        totalIDs+=game

print(totalIDs)

power = 0

for g in games:

    bag = {
        'red': 0,
        'green': 0,
        'blue': 0
    }

    game, picks = g.split(':')

    game = int(re.sub('\D', '', game))

    picks = re.sub(',', '', picks).split(';')
    picks = [pick.split() for pick in picks]

    for pick in picks:
        while len(pick) >= 2:
            num = pick.pop(0)
            col = pick.pop(0)

            if bag[col] < int(num):
                bag[col] = int(num)

    power += bag['red']*bag['blue']*bag['green']

print(power)