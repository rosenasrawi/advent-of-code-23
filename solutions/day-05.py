from _getinput import *
import regex as re

# --- Day 5: If You Give A Seed A Fertilizer ---

def list_nums(line):
    return list(map(int, re.findall(r'\d+',line)))

def find_location():

    input = getinput(day='05', example=False)
    seeds = list_nums(input.pop(0)); input.pop(0)

    for line in input:

        if 'map' in line:
            new = seeds.copy()

        if any(c.isnumeric() for c in line):

            dest, s_map, n = list_nums(line)
            e_map = s_map + n-1
            dif = dest - s_map

            for i, seed in enumerate(seeds):

                if s_map <= seed <= e_map:
                    new[i] = seed + dif
            
        if line == '' or line == input[-1]:
            seeds = new.copy()

    return min(seeds)

def find_ranges():

    input = getinput(day='05', example=True)
    seeds = list_nums(input.pop(0)); input.pop(0)
    ranges = [[seeds[i], seeds[i+1]+ seeds[i]-1] for i in range(0,len(seeds),2)]

    for line in input:

        if 'map' in line:
            new = []
        
        if any(c.isnumeric() for c in line):

            dest, s_map, n = list_nums(line)
            e_map = s_map + n-1
            dif = dest - s_map

            for i, curr_range in enumerate(ranges):
                s_range, e_range = curr_range
                
                if s_map <= s_range and e_range <= e_map:
                    
                    curr_range = [r+dif for r in curr_range]
                    new.append(curr_range)
                    ranges[i] = None
                
                if s_range < s_map and s_map <= e_range <= e_map:

                    overlap_range = [s_map, e_range]
                    overlap_range = [r+dif for r in overlap_range]
                    new.append(overlap_range)

                    out_range = [s_range, s_map-1]
                    ranges[i] = None; ranges.append(out_range)

                if s_map <= s_range <= e_map and e_range > e_map:

                    overlap_range = [s_range, e_map]
                    overlap_range = [r+dif for r in overlap_range]
                    new.append(overlap_range)

                    out_range = [e_map+1, e_range]
                    ranges[i] = None; ranges.append(out_range)
            
            ranges = [r for r in ranges if r is not None]

        if line == '' or line == input[-1]:
            new += ranges
            ranges = new.copy()
            print(ranges)

    return min(ranges)[0]

print('Part 1:', find_location())
print('Part 2:', find_ranges())