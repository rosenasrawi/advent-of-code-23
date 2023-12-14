from _getinput import *
import regex as re

# --- Day 14: Parabolic Reflector Dish ---

def find_stones(input):
    stones = []

    for r, line in enumerate(input):
        if 'O' in line:
            pos = [i for i,c in enumerate(line) if c == 'O']
            for p in pos: stones.append([r,p])
    return stones

def tilt_lever(stones, input):

    for stone in stones:
        r,c = stone
        while True:
            if r==0: break
            if input[r-1][c] == '.':
                input[r][c] = '.'
                r-=1
                input[r][c] = 'O'
            else:
                break
    
    return input

def get_load(input):
    num_stones = [line.count('O') for line in input]
    weight = list(range(len(num_stones),0,-1))

    total = 0
    for i in range(len(weight)):
        total+= weight[i]*num_stones[i]
    
    return total

input = getinput(day='14', example=False)
input = [list(line) for line in input]

stones = find_stones(input)
input = tilt_lever(stones,input)

print('Part 1:', get_load(input))