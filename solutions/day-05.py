from _getinput import *
import regex as re

# --- Day 5: If You Give A Seed A Fertilizer ---

def list_nums(line):
    return list(map(int, re.findall(r'\d+',line)))

def find_location():

    input = getinput(day='05', example=False)

    seeds = list_nums(input.pop(0)); input.pop(0)

    for line in input:

        if 'map' in line:
            new = seeds.copy()

        if any(c.isnumeric() for c in line):

            d_start, s_start, n = list_nums(line)
            s_end = s_start + n-1

            dif = d_start - s_start

            for i, seed in enumerate(seeds):

                if s_start <= seed <= s_end:
                    new[i] = seed + dif
            
        if line == '' or line == input[-1]:
            seeds = new.copy()

    return min(seeds)

print('Part 1:', find_location())