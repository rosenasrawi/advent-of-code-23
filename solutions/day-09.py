from _getinput import *

# --- Day 9: Mirage Maintenance ---

def analyze_oasis():

    oasis = getinput(day='09', example=False)
    oasis = [list(map(int,line.split())) for line in oasis]

    hist_end = 0; hist_start = 0

    for old in oasis:

        hist = [old]

        while True:
            new = [j-i for i, j in zip(old[:-1], old[1:])]
            hist.insert(0,new)

            if all(n == 0 for n in new):
                break
            old = new.copy()

        ph_end = 0; ph_start = 0

        for i in range(1,len(hist)):
            hs, he = hist[i][0], hist[i][-1]
            
            ph_end += he
            ph_start = hs - ph_start

        hist_end += ph_end
        hist_start += ph_start

    return hist_end, hist_start

hist_end, hist_start = analyze_oasis()

print('Part 1:', hist_end)
print('Part 2:', hist_start)