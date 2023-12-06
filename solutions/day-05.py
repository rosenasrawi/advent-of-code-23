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

            d_start, s_start, n = list_nums(line)
            s_end = s_start + n-1

            dif = d_start - s_start

            for i, seed in enumerate(seeds):

                if s_start <= seed <= s_end:
                    new[i] = seed + dif
            
        if line == '' or line == input[-1]:
            seeds = new.copy()

    return min(seeds)

print('Part 1:', find_location())

input = getinput(day='05', example=True)
seeds = list_nums(input.pop(0)); input.pop(0)

seeds = [[seeds[i], seeds[i+1]] for i in range(0, len(seeds), 2)]

for line in input:

    if 'map' in line:
        new = []

    if any(c.isnumeric() for c in line):

        d_start, s_start, n = list_nums(line)
        s_end = s_start + n-1

        dif = d_start - s_start

        for seed in seeds:
            s1 = seed[0]
            s2 = sum(seed)-1
            s3 = seed[1]

            start_in = s_start <= s1 <= s_end
            end_in = s_start <= s2 <= s_end

            start_left = s1 < s_start
            start_right = s1 > s_end
            
            end_left = s2 < s_start
            end_right = s2 > s_end

            # no overlap
            if start_right or end_left:
                new.append(seed)
            
            # full overlap
            if start_in and end_in:
                seed[0] += dif
                new.append(seed)

            # right overlap
            if start_left and end_in:

                len_r = s2 - s_start + 1
                len_l = s3 - len_r

                seed_r = [s_start + dif, len_r]
                seed_l = [s1, len_l]

                new.append(seed_r)
                seeds.append(seed_l)

            # left overlap
            if start_in and end_right:

                len_l = s_end - s1 + 1
                len_r = s3 - len_l

                seed_l = [s1 + dif, len_l]
                seed_r = [s_end+1, len_l]

                new.append(seed_l)
                seeds.append(seed_r)

            # mid overlap
            if start_left and end_right:

                len_m = n
                len_l = s3 - (s2 - s_start)
                len_r = s3 - (s_end - s1)

                seed_m = [s_start + dif, n]
                seed_l = [s1, len_l]
                seed_r = [s2+1, len_r]

                new.append(seed_m)
                seeds.append(seed_l)
                seeds.append(seed_r)

    if line == '' or line == input[-1]:
        seeds = new.copy()

print(seeds)


