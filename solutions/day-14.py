from _getinput import *

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

def turn_platform(input):
    return list(map(list,list(zip(*input[::-1]))))

def total_load():

    input = getinput(day='14', example=False)
    input = [list(line) for line in input]

    stones = find_stones(input)
    input = tilt_lever(stones,input)

    return get_load(input)

def find_cycle():

    input = getinput(day='14', example=False)
    input = [list(line) for line in input]

    tup_input = tuple(''.join(line) for line in input)
    states = {}; step = 1

    while True:

        for _ in range(4):
            stones = find_stones(input)
            input = tilt_lever(stones,input)
            input = turn_platform(input)

        tup_input = tuple(''.join(line) for line in input)
        
        if tup_input in states:
            first_occ = list(states.keys()).index(tup_input)
            cycle_len = len(states)-first_occ
            left = (1000000000 - len(states)-1) % cycle_len

            for _ in range(left):
                for _ in range(4):
                    stones = find_stones(input)
                    input = tilt_lever(stones,input)
                    input = turn_platform(input)

            return get_load(input)

        states[tup_input] = step
        step+=1

print('Part 1:', total_load())
print('Part 2:', find_cycle())