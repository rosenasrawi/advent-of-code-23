from _getinput import *

# --- Day 14: Parabolic Reflector Dish ---

def tilt_lever(input):

    for y, line in enumerate(input):
        for x, char in enumerate(line):

            if char == 'O':
                r,c = y,x
                while True:
                    if r==0: break
                    if input[r-1][c] == '.':
                        input[r][c] = '.'; r-=1
                        input[r][c] = 'O'
                    else: break
    
    return input

def get_load(input):
    s = [line.count('O') for line in input]
    w = list(range(len(s),0,-1))
    
    return sum([w[i]*s[i] for i in range(len(w))])

def turn_platform(input):
    return list(map(list,zip(*input[::-1])))

def total_load():

    input = getinput(day='14', example=False)
    input = [list(line) for line in input]
    input = tilt_lever(input)

    return get_load(input)

def find_cycle():

    input = getinput(day='14', example=False)
    input = [list(line) for line in input]
    t_input = tuple(tuple(line) for line in input)

    state = {}; step = 1
    
    while True:

        for _ in range(4):
            input = tilt_lever(input)
            input = turn_platform(input)

        t_input = tuple(tuple(line) for line in input)
        
        if t_input in state:
            first = list(state.keys()).index(t_input)
            cycle = len(state)-first
            left = (1000000000 - len(state)-1) % cycle

            for _ in range(left):
                for _ in range(4):
                    input = tilt_lever(input)
                    input = turn_platform(input)

            return get_load(input)

        state[t_input] = step
        step+=1

print('Part 1:', total_load())
print('Part 2:', find_cycle())