from _getinput import *

# --- Day 13: Point of Incidence ---

def get_maps(maps = [], map = []):

    input = getinput(day='13', example=False)
    
    for line in input:
        
        if line == '': 
            maps.append(map)
            map = []
        else:
            map.append(line)

    maps.append(map)

    return maps

def find_mirror(map):

    mirror = None

    for i in range(1,len(map)):
        prev = map[i-1]
        line = map[i]

        if prev == line:
            left = list(range(0,i))
            right = list(range(i,len(map)))
            left.reverse()

            mirror = list(zip(left,right))
            print(mirror)
            break

    if mirror == None:
        return 0
    
    for l,r in mirror:
        if map[l] != map[r]:
            return 0

    return i

maps = get_maps()
total = 0

for hor_map in maps:
    print('-----------------')
    for h in hor_map:
        print(h)
    
    n_hor = find_mirror(hor_map)*100
    print('hor', n_hor)

    vert_map = list(map(list, zip(*hor_map)))
    vert_map = [''.join(l) for l in vert_map]

    print('-----------------')

    for v in vert_map:
        print(v)
    
    n_vert = find_mirror(vert_map)
    print('ver', n_vert)

    total += n_hor + n_vert

print(total)

