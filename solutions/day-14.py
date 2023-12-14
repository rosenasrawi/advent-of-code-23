from _getinput import *

# --- Day 14: Parabolic Reflector Dish ---

def tilt_lever(input):

    for y, line in enumerate(input):
        for x, char in enumerate(line):

            if char == 'O':
                r,c = y,x

                while True:
                    if r==0: 
                        break
                    if input[r-1][c] == '.':
                        input[r][c] = '.'
                        r-=1
                        input[r][c] = 'O'
                    else:
                        break
    
    return input

def get_load(input):
    n_stones = [line.count('O') for line in input]
    weights = list(range(len(n_stones),0,-1))

    total = 0
    for i in range(len(weights)):
        total+= weights[i] * n_stones[i]
    
    return total

def turn_platform(input):
    return list(map(list,list(zip(*input[::-1]))))

def total_load():

    input = getinput(day='14', example=False)
    input = [list(line) for line in input]

    input = tilt_lever(input)

    return get_load(input)

def find_cycle():

    input = getinput(day='14', example=False)
    input = [list(line) for line in input]

    tup_input = tuple(''.join(line) for line in input)
    states = {}; step = 1

    while True:

        for _ in range(4):
            input = tilt_lever(input)
            input = turn_platform(input)

        tup_input = tuple(''.join(line) for line in input)
        
        if tup_input in states:
            first_occ = list(states.keys()).index(tup_input)
            cycle_len = len(states)-first_occ
            left = (1000000000 - len(states)-1) % cycle_len

            for _ in range(left):
                for _ in range(4):
                    input = tilt_lever(input)
                    input = turn_platform(input)

            return get_load(input)

        states[tup_input] = step
        step+=1

print('Part 1:', total_load())
print('Part 2:', find_cycle())