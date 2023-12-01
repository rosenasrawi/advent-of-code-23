from _getinput import *
import regex as re

calibration = getinput(day = '01')

def sum_nums(calibration, inclwords = False):

    word2num = {'one': 1, 'two': 2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    pattern = '|'.join(word2num.keys())

    calib_int = []

    for c in calibration:

        if inclwords:
            numbers = re.findall(rf'{pattern}|\d', c, overlapped=True)
            numbers = [str(word2num[num]) if num in word2num.keys() else num for num in numbers]

        else: 
            numbers = re.findall(r'\d', c)

        numbers = int(numbers[0]+numbers[-1])

        calib_int.append(numbers)

    return sum(calib_int)

print('Part 1:', sum_nums(calibration))
print('Part 2:', sum_nums(calibration, inclwords=True))