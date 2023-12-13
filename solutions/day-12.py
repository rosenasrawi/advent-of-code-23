from _getinput import *
from functools import cache

# --- Day 12: Hot Springs ---

@cache
def check_group(springs, counts, g_id = -1, count = 0):

    for i, s in enumerate(springs):

        if s == '#':
            if count == 0:
                g_id+=1
            if g_id > len(counts)-1:
                return 0
            count += 1
            
            if count > counts[g_id]:
                return 0
        
        elif s == '.':
            if 0 < count < counts[g_id]:
                return 0
            count = 0

        elif s == '?':
            if g_id >= 0 and 0 < count < counts[g_id]:
                count += 1
            elif g_id >= 0 and count == counts[g_id]:
                count = 0
            else:
                dmgd = check_group('#' + springs[i+1:], counts, g_id, count)
                oprt = check_group( '.' + springs[i+1:], counts, g_id, count)

                return dmgd + oprt
            
    if count == 0 and g_id == len(counts)-1:
        return 1
    elif count == counts[-1] and g_id == len(counts)-1:
        return 1
    else:
        return 0

input = getinput(day='12',example=False)
input = [line.split() for line in input]

input = [[springs, 
          list(map(int, counts.split(',')))]
          for springs, counts in input]

total = 0
for springs, counts in input:
    total += check_group(springs, tuple(counts))

print(total)