from _getinput import *

# --- Day 10: Pipe Maze ---

moves = {
    'N': {'7':'W', '|':'N' , 'F':'E'},
    'S': {'J':'W', '|':'S' , 'L':'E'},
    'W': {'L':'N', '-':'W' , 'F':'S'},
    'E': {'J':'N', '-':'E' , '7':'S'},
}

update = {'N': (-1,0), 'S': (1,0), 'W': (0,-1), 'E': (0,1)}

def get_start():
    input = getinput(day='10', example=False)
    input = [list(line) for line in input]
    rl = len(input); cl = len(input[0])

    for r in range(rl):
        for c in range(cl):
            if input[r][c] == 'S':
                start = [r,c]
                break

    return start, input

def find_first():

    start, input = get_start()

    r,c = start

    adj = [[r-1,c], [r+1,c], [r,c-1], [r,c+1]]
    next = [input[r][c] for r,c in adj]
    dirs = list(moves.keys())

    for i, pipe in enumerate(next):
        dir = dirs[i]
        cango = moves[dir]

        if pipe in cango:
            pos = adj[i]
            dir = cango[pipe]

            current = (pipe,pos,dir)
            break

    return current, input

def find_loop():
    
    current, input = find_first()
    steps = 2

    while True:

        pipe, pos, dir = current

        rd, cd = update[dir]
        pos = [pos[0]+rd, pos[1]+cd]

        pipe = input[pos[0]][pos[1]]
        if pipe == 'S': break

        dir = moves[dir][pipe]

        current = (pipe,pos,dir)
        steps+=1
    
    return steps//2

print('Part 1:', find_loop())