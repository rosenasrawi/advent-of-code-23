from _getinput import *

# --- Day 16: The Floor Will Be Lava ---

def get_mirrors():

    input = getinput(day='16', example=False)

    mirror = {
        '/': {'r':'u', 'l':'d', 'u':'r', 'd':'l'},
        '\\': {'r':'d', 'l':'u', 'u':'l', 'd':'r'},
        '-': {'r':'r', 'l':'l', 'u':('l','r'), 'd':('l','r')},
        '|': {'u':'u', 'd':'d', 'l':('u','d'), 'r':('u','d')}
    }

    dir = {'r':(0,1), 'l': (0,-1), 'u': (-1,0), 'd': (1,0)}

    return input, dir, mirror

def the_shining(start):

    splits = [['.'] * cmax for _ in range(rmax)]
    light = [['.'] * cmax for _ in range(rmax)]
    beam = [start]

    while True:

        if not beam: 
            break

        r,c, dis = beam.pop()
        
        if splits[r][c] == 'x':
            continue

        light[r][c] = 'x'
        mir = input[r][c]

        if mir in mirror:
            dis = mirror[mir][dis]
        if len(dis) == 1: 
            dis = (dis)

        y, x, ns = r, c, 0

        for d in dis:
            yd, xd = dir[d]

            if 0 <= y+yd < rmax and 0 <= x+xd < cmax:
                beam.append((y+yd, x+xd, d))
                ns+=1
        
        if ns == 2:
            splits[r][c] = 'x'

    return sum([l.count('x') for l in light])

def get_edges(edges=[]):

    edges += [(0,c,'d') for c in range(cmax)]
    edges += [(rmax-1,c,'u') for c in range(cmax)]
    edges += [(r,0,'l') for r in range(rmax)]
    edges += [(r,cmax-1,'r') for r in range(rmax)]

    return edges

input, dir, mirror = get_mirrors()
rmax, cmax = len(input[0]), len(input)

print('Part 1:', the_shining((0,0,'r')))
print('Part 2:', max([the_shining(s) for s in get_edges()]))