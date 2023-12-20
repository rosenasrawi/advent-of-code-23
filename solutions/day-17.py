from _getinput import *
import heapq, time

# --- Day 17: Clumsy Crucible ---

def find_path(ultra = False):

    t1 = time.time()
    input = getinput(day='17', example=False)
    end = (len(input)-1, len(input[0])-1)

    score, start, ploc = 0, (0, 0, None), (None, None)
    pdir = 'N'*3 if not ultra else 'N'*10

    queue = [(score, start, ploc, pdir)]
    memory = set()

    while queue:
        score, current, ploc, pdir = heapq.heappop(queue)

        if (current, pdir) in memory:
            continue
        
        r, c, dir = current
        if (r, c) == end:
            return score, round(time.time()-t1,3)

        memory.add((current, pdir))

        around = [(r,c-1,'l'), (r-1,c,'u'), (r,c+1,'r'), (r+1,c,'d')]

        around = [a for a in around if 0<=a[0]<=end[0] and 0<=a[1]<=end[1]]
        around = [a for a in around if (a[0],a[1]) != ploc]

        if len(set(pdir)) == 1:
            around = [a for a in around if a[-1] != dir]

        if ultra:
            last = pdir[6:]
            if len(set(last)) != 1 and last[-1]!='N':
                around = [a for a in around if a[-1] == dir]

        ploc = (r,c)

        for next in around:
            rn, cn, dn = next
            nscore = score + int(input[rn][cn])

            if (next, pdir[1:]+dn) in memory:
                continue

            heapq.heappush(queue, (nscore, next, ploc, pdir[1:]+dn))

print('Part 1:', find_path())
print('Part 2:', find_path(ultra = True))