from _getinput import *
import re

# --- Day 19: Aplenty ---

def parse_hell():

    input = getinput(day='19',example=False)
    
    parts  = input[input.index('')+1:]
    parts = [p.replace('=',':') for p in parts]
    parts = [re.sub(r'([a-z])', r"'\1'", p) for p in parts]
    parts = [eval(p) for p in parts]

    workflow = input[:input.index('')]
    rules = {}

    for flow in workflow:
        item, rule = flow[:-1].split('{')
        rule = rule.split(',')
        rule = [r.split(':') for r in rule]

        rules[item] = rule

    return parts, rules

def eval_part(part, rules):

    item = 'in'

    while True:

        if item == 'A': return True
        if item == 'R': return False
        
        rule = rules[item]

        for rl in rule:

            if len(rl) == 2:
                r, item = rl
                r = r.replace(r[0], str(part[r[0]]))

                if eval(r):
                    break

            else:
                item = rl[0]
                break

def move_parts(accept = 0):

    parts, rules = parse_hell()

    for part in parts:
        if eval_part(part, rules):
            accept += sum([p for p in part.values()])

    return accept

print('Part 1:', move_parts())