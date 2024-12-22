#!/usr/bin/env python3
import re
from collections import defaultdict
from collections import deque

def nums(v):
	return [int(x) for x in re.findall("\d+",v)]

D = [(-1,0), (0, 1), (1, 0), (0,-1)]

file1 = '19.in'
#file1 = '19.test'

#input = [x.strip() for x in open(file1, 'r').readlines()]
input = open(file1, 'r').read().strip()
patterns, target = input.split("\n\n")
P = patterns.split(', ')
T = target.split("\n")
regex = "|".join(P)
print(regex)
prog = re.compile('(' + regex + ')+')


DP = {}
def is_valid(v):
#    print(v)
    if v in DP:
        return DP[v]
    if len(v) == 0:
        return True
    for p in P:
        if v.startswith(p) and is_valid(v[len(p):]):
            DP[v] = True
            return True
    DP[v] = False
    return False

p1 = 0
for t in T:
    print(t)
#    if not None == prog.fullmatch(t):
    if is_valid(t):
        print(t)
        p1+=1

print('p1',p1)
