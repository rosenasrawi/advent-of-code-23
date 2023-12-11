from _getinput import *

# --- Day 11: Cosmic Expansion ---

def insert_empty(input):
    
    skip = False

    for r, line in enumerate(input):
        if skip:
            skip=False
            continue
        if '#' not in line:
            input.insert(r,line)
            skip = True

    return input

def cosmic_expansion():

    input = getinput(day='11', example=False)

    for _ in range(2):
        input = insert_empty(input)
        input = list(map(list, zip(*input)))
    
    galaxies = []

    for r, line in enumerate(input):
        for c, g in enumerate(line):
            if g == '#': galaxies.append((r,c))

    return galaxies

def find_path(g1, g2):

    r1, c1 = g1
    r2, c2 = g2

    rd = 1 if r2-r1 > 0 else -1
    cd = 1 if c2-c1 > 0 else -1

    steps = 0

    while True:
        if r1 == r2: rd = 0
        if c1 == c2: cd = 0

        if cd == 0 and rd == 0:
            break

        r1+=rd; c1+=cd
        if rd == 0 or cd == 0:
            steps += 1
        else: steps += 2
    
    return steps

def connect_galaxy():

    galaxies = cosmic_expansion()
    total = 0

    while galaxies:
        g1 = galaxies.pop(0)

        for g2 in galaxies:
            total += find_path(g1,g2)
        
    return total

print('Part 1:', connect_galaxy())



    
