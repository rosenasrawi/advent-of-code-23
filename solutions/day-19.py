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

def move_parts():

    parts, rules = parse_hell()
    A, item = [], 'in'

    for part in parts:
        rule = rules[item].copy()

        while rule:
            it = rule.pop(0)

            if it == ['A']:
                A.append(part); break
            if it == ['R']: break

            if len(it) == 2:
                r, it = it
                r = r.replace(r[0], str(part[r[0]]))

                if eval(r):
                    if it == 'A':
                        A.append(part); break
                    if it == 'R': break
                    else:
                        rule = rules[it].copy()
                        continue
            else:
                rule = rules[it[0]].copy()
                continue

    return sum([sum(p.values()) for p in A])

print('Part 1:', move_parts())