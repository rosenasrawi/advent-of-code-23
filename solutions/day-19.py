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

def get_combo(ranges, accept=1):

    for let in 'xmas':
        low, high = ranges[let]
        accept *= high-low+1
    
    return accept

def eval_range(item, ranges, rules):

    if item == 'A':
        return get_combo(ranges)
    if item == 'R':
        return 0
    
    accept = 0
    rule = rules[item]

    for rl in rule:

        if len(rl) == 2:
            r, item = rl
            low, high = ranges[r[0]]
            rng_yes = ranges.copy()

            if '<' in r:
                let, num = r.split('<')
                
                rng_yes[let] = [low, int(num)-1]
                ranges[let] = [int(num), high]

            elif '>' in r:
                let, num = r.split('>')
                
                ranges[let] = [low, int(num)]
                rng_yes[let] = [int(num)+1, high]

            accept += eval_range(item, rng_yes, rules)
        
        else:
            item = rl[0]
            accept += eval_range(item, ranges, rules)

    return accept

def move_ranges():

    _, rules = parse_hell()
    item, ranges = 'in', {let:[1,4000] for let in 'xmas'}

    return eval_range(item, ranges, rules)

print('Part 1:', move_parts())
print('Part 2:', move_ranges())