from _getinput import *

# --- Day 13: Point of Incidence ---

def get_maps():

    input = getinput(day='13', example=False)
    maps = []; map = []

    for line in input:
        if line == '': 
            maps.append(map); map = []
        else:
            map.append(line)

    maps.append(map)

    return maps

def check_reflection(map):

    mirror, smudge = 0, 0

    for i in range(1,len(map)):

        left = list(range(0,i)); left.reverse()
        right = list(range(i,len(map)))

        difference = 0
        combos = list(zip(left,right))

        for l,r in combos:
            l = map[l]; r = map[r]
            difference += sum([l[j]!=r[j] for j in range(len(l))])

        if difference == 0:
            mirror = i
        if difference == 1:
            smudge = i

    return mirror, smudge

def find_mirrors():

    maps = get_maps()
    mirror, smudge = 0, 0

    for hor_map in maps:
        
        vert_map = list(map(list, zip(*hor_map)))

        m_hor, s_hor = check_reflection(hor_map)
        m_vert, s_vert = check_reflection(vert_map)

        mirror += m_hor*100 + m_vert
        smudge += s_hor*100 + s_vert

    return mirror, smudge

mirror, smudge = find_mirrors()

print('Part 1:', mirror)
print('Part 2:', smudge)