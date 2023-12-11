from _getinput import *

# --- Day 10: Pipe Maze ---

def get_start():

    input = getinput(day='10', example=False)
    input = [list(line) for line in input]

    for line in input:
        if 'S' in line:
            r = input.index(line)
            c = line.index('S')
            adj = [[r-1,c], [r+1,c], [r,c-1], [r,c+1]]

            return adj, [r,c], input

def find_loop():
    
    loop = []

    moves = {
        'n': {'7':'w', '|':'n' , 'F':'e'},
        's': {'J':'w', '|':'s' , 'L':'e'},
        'w': {'L':'n', '-':'w' , 'F':'s'},
        'e': {'J':'n', '-':'e' , '7':'s'},
    }

    update = {
        'n': (-1,0), 's': (1,0), 
        'w': (0,-1), 'e': (0,1)
    }

    adj, start, input = get_start()
    loop.append(start)

    for i, pos in enumerate(adj):
        pipe = input[pos[0]][pos[1]]
        cango = moves[list(moves.keys())[i]]

        if pipe in cango:
            current = (pos, pipe, cango[pipe])
            break

    steps = 2
    
    while True:

        pos, pipe, dir = current
        loop.append(pos)
        rd, cd = update[dir]
        
        pos = [pos[0]+rd, pos[1]+cd]
        pipe = input[pos[0]][pos[1]]

        if pipe == 'S': break

        dir = moves[dir][pipe]

        current = (pos, pipe, dir)
        steps+=1
    
    return steps//2, loop, input

def find_inner(loop, input):

    enclosed = 0
    cmax = len(input[0])
    rmax = len(input)
    loop_set = set(map(tuple, loop))

    for r, line in enumerate(input):
        for c, pipe in enumerate(line):
            
            if (r, c) in loop_set:
                continue
            
            crosses = 0
            r2, c2 = r, c

            while c2 < cmax and r2 < rmax:

                pipe = input[r2][c2]
                
                if (r2, c2) in loop_set and pipe not in ['L', '7']:
                    crosses += 1
                
                r2 += 1
                c2 += 1

            if crosses % 2 == 1:
                enclosed += 1
                
    return enclosed

steps, loop, input = find_loop()

print('Part 1:', steps)
print('Part 1:', find_inner(loop, input))
