from _getinput import *

# --- Day 18: Lavaduct Lagoon ---

def dig_lagoon(expand = False):

    input = getinput(day='18', example=False)
    input = [line.split() for line in input]

    if expand:
        input = [line[-1] for line in input]
        d = {'0':'R', '1':'D', '2':'L', '3':'U'}

        for i, line in enumerate(input):
            input[i] = (d[line[-2]], int(line[2:-2],16))

    else:
        input = [(dir,int(steps)) for dir, steps, _ in input]

    dirs = {'R':(0,1), 'L': (0,-1), 'U': (-1,0), 'D': (1,0)}
    
    digs = [(0,0)]
    r,c = 0,0
    area = 0

    for dir, steps in input:

        rd, cd = dirs[dir]
        r += rd * steps; c += cd * steps
        
        digs.append((r,c))
        area+=steps

    return digs[:-1], area

def fill_lagoon(expand=False):

    digs, area = dig_lagoon(expand)

    def shoelace(coord, area = 0):

        for i in range(len(coord)):
            area += coord[i][0] * (coord[i - 1][1] - coord[(i + 1) % len(coord)][1])

        return abs(area) // 2

    area += shoelace(digs) - area // 2 + 1

    return area

print('Part 1:', fill_lagoon())
print('Part 2:', fill_lagoon(expand = True))