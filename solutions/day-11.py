from _getinput import *

# --- Day 11: Cosmic Expansion ---

def update_galaxies(input, galaxies, factor, flip = False):
    
    if flip: 
        input = list(map(list, zip(*input)))
        pos = 1
    else: pos = 0
    
    count = 0
    for r, line in enumerate(input):
        if '#' not in line:
            for i in range(len(galaxies)):
                if galaxies[i][pos] > r+count:
                    galaxies[i][pos] += factor-1
            count += factor-1
    
    return galaxies

def cosmic_expansion(factor = 2):

    input = getinput(day='11', example=False)

    galaxies = []

    for r, line in enumerate(input):
        for c, g in enumerate(line):
            if g == '#': galaxies.append([r,c])

    galaxies = update_galaxies(input, galaxies, factor)
    galaxies = update_galaxies(input, galaxies, factor, flip = True)
    
    return galaxies

def find_path(g1, g2):

    r1, c1 = g1
    r2, c2 = g2

    steps = abs(r1-r2) + abs(c1-c2)

    return steps

def connect_galaxy(factor):

    galaxies = cosmic_expansion(factor)
    total = 0

    while galaxies:
        g1 = galaxies.pop(0)

        for g2 in galaxies:
            total += find_path(g1,g2)
        
    return total

print('Part 1:', connect_galaxy(factor = 2))
print('Part 2:', connect_galaxy(factor = 1000000))