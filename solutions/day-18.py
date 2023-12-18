from _getinput import *

# --- Day 18: Lavaduct Lagoon ---

def dig_out():

    input = getinput(day='18',example=False)
    input = [line.split() for line in input]

    dirs = {'R':(0,1), 'L': (0,-1), 'U': (-1,0), 'D': (1,0)}
    digs = {(0,0)}; start = (0,0)

    for dir, steps, _ in input:

        r, c = start
        rd, cd = dirs[dir]

        for _ in range(int(steps)):
            r+=rd; c+=cd
            digs.add((r,c))

        start = (r,c)

    rmin, cmin = min(r for r,_ in digs), min(c for _,c in digs)
    digs = [(r + abs(rmin), c + abs(cmin)) for r, c in digs]

    rmax, cmax = max(r for r,_ in digs), max(c for _,c in digs)
    digmap = [['🎄']*(cmax+1) for _ in range(rmax+1)]

    for r,c in digs:
        digmap[r][c] = '🎁'
    
    return digmap, len(digs)

def fill_lagoon():

    digmap, outline = dig_out()

    def find_start(pattern = '🎄🎁🎄'):

        for r, line in enumerate(digmap):
            for c in range(len(line)):
                if ''.join(line[c-1:c+2]) == pattern:
                    return (r,c+1)

    surround = [(0,1),(1,0),(0,-1),(-1,0),
                (1,1),(-1,-1),(-1,1),(1,-1)]

    filled = set()
    queue = {find_start()}

    while queue:
        r,c = queue.pop()
        filled.add((r,c))

        for rd, cd in surround:
            next = digmap[r+rd][c+cd]
            i_next = (r+rd, c+cd)

            if i_next not in filled:
                if next != '🎁':
                    queue.add(i_next)

    return outline + len(filled)

print('Part 1:', fill_lagoon())