from _getinput import *
import regex as re

# --- Day 2: Cube Conundrum ---

def get_games():

    games = getinput('02', example=False)

    for i, line in enumerate(games):

        game, picks = line.split(':')

        game = int(re.sub('\D', '', game))

        picks = re.sub(',', '', picks).split(';')
        picks = [pick.split() for pick in picks]

        games[i] = [game, picks]
    
    return games


def test_games():

    games = get_games()

    bag = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

    totalIDs = 0

    for round in games:
        game, picks = round

        for pick in picks:

            while pick:
                num = int(pick.pop(0))
                col = pick.pop(0)

                impossible = bag[col] < num

                if impossible: break
            
            if impossible: break

        if not impossible: 
            totalIDs+=game

    return totalIDs

def get_power():

    games = get_games()

    power = 0

    for round in games:

        bag = {
            'red': 0,
            'green': 0,
            'blue': 0
        }

        game, picks = round

        for pick in picks:
            while len(pick) >= 2:
                num = pick.pop(0)
                col = pick.pop(0)

                if bag[col] < int(num):
                    bag[col] = int(num)

        power += bag['red']*bag['blue']*bag['green']

    return power

print('Part 1:', test_games())
print('Part 2:', get_power())