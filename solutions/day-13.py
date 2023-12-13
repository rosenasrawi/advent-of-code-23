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

def find_mirror(map):

    mirror, smudge = 0, 0

    for i in range(1,len(map)):

        left = list(range(0,i))
        left.reverse()
        right = list(range(i,len(map)))

        combos = list(zip(left,right))
        difference = 0

        for l,r in combos:
            l = map[l]; r = map[r]
            difference += sum([l[j]!=r[j] for j in range(len(l))])

        if difference == 0:
            mirror = i
        
        if difference == 1:
            smudge = i

    return mirror, smudge

def get_reflect():

    maps = get_maps()
    reflection, smudge = 0, 0

    for hor_map in maps:
        
        m_hor, s_hor = find_mirror(hor_map)

        vert_map = list(map(list, zip(*hor_map)))
        m_vert, s_vert = find_mirror(vert_map)

        reflection += m_hor*100 + m_vert
        smudge += s_hor*100 + s_vert

    return reflection, smudge

reflection, smudge = get_reflect()

print('Part 1:', reflection)
print('Part 2:', smudge)