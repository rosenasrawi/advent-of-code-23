from _getinput import *
import regex as re


# --- Day 8: Haunted Wasteland ---

def get_map():
    input = getinput(day='08', example=False)
    dirs = list(input.pop(0)); input.pop(0)
    map = {}

    for line in input:
        source, left, right = re.findall(r'\b[A-Z0-9]+', line)
        map[source] = (left,right)

    return map, dirs

def nav_wasteland():

    map, dirs = get_map()
    steps = 0; pos = 'AAA'

    while dirs:
        d = dirs.pop(0); dirs.append(d)
        l, r = map[pos]

        pos = l if d == 'L' else r
        steps+=1

        if pos == 'ZZZ':
            break

    return steps

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def nav_sim_wasteland():

    map, dirs = get_map()
    start = [pos for pos in list(map.keys()) if pos.endswith('A')]
    steps = []

    for pos in start:

        sim_step = 0

        while dirs:
            d = dirs.pop(0); dirs.append(d)
            l, r = map[pos]

            pos = l if d == 'L' else r
            sim_step+=1

            if pos.endswith('Z'):
                break

        steps.append(sim_step)
    
    a = steps.pop(0)
    for b in steps:
        a = lcm(a,b)

    return a

print('Part 1:', nav_wasteland())
print('Part 2:', nav_sim_wasteland())