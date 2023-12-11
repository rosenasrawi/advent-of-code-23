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

            return adj, input

def find_loop():
    
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

    adj, input = get_start()

    for i, pos in enumerate(adj):
        pipe = input[pos[0]][pos[1]]
        cango = moves[list(moves.keys())[i]]

        if pipe in cango:
            current = (pos, pipe, cango[pipe])
            break

    steps = 2
    
    while True:

        pos, pipe, dir = current
        rd, cd = update[dir]
        
        pos = [pos[0]+rd, pos[1]+cd]
        pipe = input[pos[0]][pos[1]]

        if pipe == 'S': break

        dir = moves[dir][pipe]

        current = (pos, pipe, dir)
        steps+=1
    
    return steps//2

print('Part 1:', find_loop())