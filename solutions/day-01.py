from _getinput import *
import regex as re

calibration = getinput(day = '01')

def get_sum(calibration, word_incl = False):

    word2num = {
        'one': '1', 
        'two': '2', 
        'three': '3', 
        'four': '4', 
        'five': '5', 
        'six': '6', 
        'seven': '7', 
        'eight': '8', 
        'nine': '9'
    }

    words = '|'.join(word2num.keys())

    calib_sum = 0

    for c in calibration:

        if word_incl:
            nums = re.findall(rf'{words}|\d', c, overlapped=True)
            nums = [word2num[n] if n in word2num.keys() else n for n in nums]

        else: 
            nums = re.findall(r'\d', c)

        calib_sum += int(nums[0]+nums[-1])

    return calib_sum

print('Part 1:', get_sum(calibration))
print('Part 2:', get_sum(calibration, word_incl=True))