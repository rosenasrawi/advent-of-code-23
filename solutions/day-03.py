from _getinput import *

import regex as re

# --- Day 3: Gear Ratios ---

def get_engine(border = False):

    engine = getinput(day = '03', example=False)

    if border:
        engine = ['.' + line + '.' for line in engine]
        newline = '.' * int(len(engine)+1)

        engine.insert(0, newline)
        engine.append(newline)

    return engine

def is_symbol(char):

    if char.isnumeric() or char == '.':
        return False
    else: 
        return True

def find_parts():

    engine = get_engine(border = True)

    total = 0

    for row, line in enumerate(engine):

        nums = re.findall(r'\d+', line)
        cols = re.finditer(r'\d+', line)

        index = [(row, c.start(0)) for c in cols]

        for i, num in enumerate(nums):

            row, col = index[i]

            around = ''

            above = engine[row-1][col-1:col+len(num)+1]
            left = engine[row][col-1]
            right = engine[row][col+len(num)]
            below = engine[row+1][col-1:col+len(num)+1]

            around += above + left + right + below

            is_part = any(is_symbol(c) for c in around)

            if is_part:
                total += int(num)

    return total

print('Part 1:', find_parts())
