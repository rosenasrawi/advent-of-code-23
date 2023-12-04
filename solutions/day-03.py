from _getinput import *
import regex as re

# --- Day 3: Gear Ratios ---

def get_engine():

    engine = getinput(day = '03', example=False)

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

    engine = get_engine()

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

            if any(is_symbol(c) for c in around):
                total += int(num)

    return total

def find_gears():

    engine = get_engine()

    gear_ratio = 0

    for row, line in enumerate(engine):

        gears = [c.start(0) for c in re.finditer(r'[*]', line)]

        if gears != []:
        
            for g in gears:

                adj_nums, num_around, i_around = [], [], []

                num_around += re.findall(r'\d+', engine[row-1])
                num_around += re.findall(r'\d+', engine[row])
                num_around += re.findall(r'\d+', engine[row+1])

                i_around += [(c.start(0), c.end(0)-1) for c in re.finditer(r'\d+', engine[row-1])]
                i_around += [(c.start(0), c.end(0)-1) for c in re.finditer(r'\d+', engine[row])]
                i_around += [(c.start(0), c.end(0)-1) for c in re.finditer(r'\d+', engine[row+1])]

                for i, num in enumerate(num_around):
                    start, end = i_around[i]

                    if g-1 <= end <= g+1 or g-1 <= start <= g+1:
                        adj_nums.append(int(num))

                if len(adj_nums) == 2:
                    gear_ratio += adj_nums[0]*adj_nums[1]

    return gear_ratio
    
print('Part 1:', find_parts())
print('Part 2:', find_gears())