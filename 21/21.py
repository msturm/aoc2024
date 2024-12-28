#!/usr/bin/env python3
import re
from collections import defaultdict
from collections import deque

def nums(v):
	return [int(x) for x in re.findall("\d+",v)]

D = [(-1,0), (0, 1), (1, 0), (0,-1)]

file1 = '21.in'
# file1 = '21.test'

input = [x.strip() for x in open(file1, 'r').readlines()]

# This url helped me a lot with solving this problem https://observablehq.com/@jwolondon/advent-of-code-2024-day-21
# Part 2 was very tough.

# we just need to get the shortest path for a sequence
# numeric keypad: (r, c) coordinates
numeric = {'7': (0,0), '8': (0,1), '9': (0,2), '4': (1,0), '5': (1,1), '6': (1,2), '1': (2,0), '2': (2,1), '3': (2,2), '0': (3,1), 'A': (3,2)}

directional = {'^': (0,1), 'A': (0,2), '<': (1,0), 'v': (1,1), '>': (1,2)}

def find_numeric_paths(v, start):
    r, c = numeric[start]
    right, left, up, down = '','','',''
    Q = deque([''])
    prev = start 
    for x in v:
        left, right, up, down = '', '', '', '' 
        rr, cc = numeric[x]
        dr = rr - r
        dc = cc - c
        if dc > 0:
            right = '>' * abs(dc)
        if dr < 0:
            up = '^' * abs(dr)
        if dc < 0:
            left = '<' * abs(dc)
        if dr > 0:
            down = 'v' * abs(dr)
        NQ = deque()
        while Q: 
            paths = Q.pop()
            if len(right) > 0 and len(up) > 0:
                    NQ.append(paths + right + up + 'A')
                    NQ.append(paths + up + right + 'A')
            elif len(left) > 0 and len(up) > 0:
                if prev in ['0','A'] and x in ['7','4','1']:
                    NQ.append(paths + up + left + 'A')
                else:
                    NQ.append(paths + left + up + 'A')
                    NQ.append(paths + up + left + 'A')
            elif len(right) > 0 and len(down) > 0:
                if x in ['0','A'] and prev in ['7','4','1']:
                    NQ.append(paths + right + down + 'A')
                else:
                    NQ.append(paths + right + down + 'A')  
                    NQ.append(paths + down + right + 'A')
            elif len(left) > 0 and len(down) > 0:
                NQ.append(paths + left + down + 'A') 
                NQ.append(paths + down + left + 'A')
            else: # only one direction
                if len(left) > 0:
                    NQ.append(paths + left + 'A')
                if len(right) > 0:
                    NQ.append(paths + right + 'A')
                if len(up) > 0:
                    NQ.append(paths + up + 'A')
                if len(down) > 0:
                    NQ.append(paths + down + 'A')
        Q = NQ
        prev = x
        r, c = numeric[x]

    return Q


# def find_directional_path(v, start):
#     r, c = directional[start]
#     path = ''
#     for x in v:
#         new_path = ''
#         rr, cc = directional[x]
#         dr = rr - r
#         dc = cc - c
#         if dc > 0:
#             new_path += '>' * abs(dc)
#         if dr > 0:
#             new_path += 'v' * abs(dr)
#         if dc < 0:
#             new_path += '<' * abs(dc)
#         if dr < 0:
#             new_path += '^' * abs(dr)
#
#         new_path += 'A'
#         r, c = directional[x]
#         path += new_path
#     return path

p1 = 0
p2 = 0


indirect2 = {('A','>'):'vA',
             ('A','<'):'v<<A',
             ('A','v'):'<vA',
             ('A','^'):'<A',
             ('A','A'):'A',
             ('v','A'):'^>A',
             ('v','<'):'<A',
             ('v','v'):'A',
             ('v','^'):'^A',
             ('v','>'):'>A',
             ('<','A'):'>>^A',
             ('<','<'):'A',
             ('<','v'):'>A',
             ('<','^'):'>^A',
             ('<','>'):'>>A',
             ('^','A'):'>A',
             ('^','<'):'v<A',
             ('^','v'):'vA',
             ('^','^'):'A',
             ('^','>'):'v>A',
             ('>','A'):'^A',
             ('>','<'):'<<A',
             ('>','v'):'<A',
             ('>','^'):'<^A',
             ('>','>'):'A'}



def expand_count(ans_count):
    # This function expands the level of robots by updating the frequency count
    # It looks at the current freuqency and creates a new list with the new combinations and the frequency
    new_frequency_count = defaultdict(int)
    for code, count in ans_count.items():
        prev_button = 'A'
        for button in code:
            if prev_button == button:
                new_key = 'A'
            else:
                new_key = indirect2[(prev_button, button)]
            prev_button = button
            new_frequency_count[new_key] += count

    return new_frequency_count


def add_indirection1(p, steps=2):
    ans_count = defaultdict(int)
    # break up in steps (p is the input for the numbers). We split on A, which gives 4 steps
    for p in [x + 'A' for x in p.split('A')[:-1]]:
        ans_count[p] += 1
    new_length = 0

    # go over the indirection for x steps
    for x in range(steps):
        ans_count = expand_count(ans_count)

    # calculate the new length
    for key, value in ans_count.items():
        new_length += value * len(key)
    return new_length



for v in input:
    inp = find_numeric_paths(v, 'A')
    num_v = nums(v)[0]
    ans_p2 = float('inf')
    ans_p1 = float('inf')
    for p in inp:
        inp = p
        # inp2 = add_indirection1(inp, 25)
        ans_p1 = min(ans_p1, add_indirection1(inp, 2))
        ans_p2 = min(ans_p2, add_indirection1(inp, 25))
    print(v, num_v, ans_p2)
    p2 += num_v * ans_p2
    p1 += num_v * ans_p1

print('p1', p1)
print('p2', p2)

