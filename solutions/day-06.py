from _getinput import *
import regex as re

# --- Day 6: Wait For It ---

def beat_record():
    
    input = getinput(day='06', example=False)
    time, distance = [list(map(int, re.findall(r'\d+',line))) for line in input]

    beaten = 1

    for i, t in enumerate(time):
        dist = distance[i]
        record = 0

        for press in range(t+1):
            if (t-press) * press > dist:
                record+=1

        beaten*=record

    return beaten

def beat_big_record():

    input = getinput(day='06', example=True)
    time, dist = [int(''.join(re.findall(r'\d',line))) for line in input]

    record = 0

    for press in range(time+1):
        if (time-press) * press > dist:
            record+=1

    return record

print('Part 1:', beat_record())
print('Part 2:', beat_big_record())
