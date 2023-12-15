from _getinput import *

# --- Day 15: Lens Library ---

def HASH(string, val = 0):

    for s in string:
        val += ord(s)
        val *= 17
        val %= 256
    
    return val

def get_initseq(total = 0):

    input = getinput(day='15',example=False).split(',')

    for string in input:
        total += HASH(string)

    return total

def HASHMAP(boxes = {}):

    input = getinput(day='15',example=False).split(',')

    for string in input:

        if '=' in string:
            t, foc = string.split('=')
        else: t = string[:-1]
        
        box = HASH(t)

        if box not in boxes:
            boxes[box] = []

        lens = boxes[box]

        if '=' in string:
            if not any(t == l[:-1] for l in lens):
                boxes[box].append(t+foc)
            else:
                for i, l in enumerate(lens):
                    if t == l[:-1]:
                        lens[i] = t+foc

        else:
            for i, l in enumerate(lens):
                if t == l[:-1]:
                    lens.pop(i)
        
    return boxes

def focus_power(power = 0):

    boxes = HASHMAP()

    for box, lens in boxes.items():
        for i, lens in enumerate(lens):
            power += (box+1) * (i+1) *  int(lens[-1])

    return power

print('Part 1:', get_initseq())
print('Part 2:', focus_power())