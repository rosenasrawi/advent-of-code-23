from _getinput import *

# --- Day 12: Hot Springs ---

def check_group(springs, counts, memo, g_id = -1, count = 0):
    
    this_try = (springs, g_id, count)

    if this_try in memo:
        return memo[this_try]

    for i, s in enumerate(springs):

        if s == '#':

            if count == 0: # new group
                g_id+=1
            if g_id > len(counts)-1: # too many groups
                return 0
            
            count += 1 # add to group
            
            if count > counts[g_id]: # larger than current group
                return 0
        
        elif s == '.':

            if 0 < count < counts[g_id]: # closed and smaller than current group
                return 0
            
            count = 0 # end the group

        elif s == '?':

            if g_id >= 0 and 0 < count < counts[g_id]: # group not yet filled
                count += 1
            elif g_id >= 0 and count == counts[g_id]: # group already filled
                count = 0

            else:
                damaged = '#' + springs[i+1:]

                dmgd = check_group(damaged, counts, memo, g_id, count)
                memo[(damaged, g_id, count)] = dmgd

                operational = '.' + springs[i+1:]

                oprt = check_group(operational, counts, memo, g_id, count)
                memo[(operational, g_id, count)] = oprt

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
    memo = {}
    total += check_group(springs, counts, memo)

print(total)