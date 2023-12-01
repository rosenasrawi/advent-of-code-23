import os

def getinput(day, example = False):

    if example: prefix = 'example-'
    else: prefix = 'input-'

    with open(os.getcwd() + '/input/' + prefix + day + '.txt', "r") as input:
        data = input.readlines()
        data = [i.rstrip('\n') for i in data]
        if len(data) == 1: data = data[0]

    return data