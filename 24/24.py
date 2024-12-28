#!/usr/bin/env python3
import re
from collections import defaultdict
from collections import deque

def nums(v):
	return [int(x) for x in re.findall("\d+",v)]

D = [(-1,0), (0, 1), (1, 0), (0,-1)]

file1 = '24.in'
#file1 = '24.test2'

#input = [x.strip() for x in open(file1, 'r').readlines()]
input = open(file1, 'r').read().strip()
wires_str, gates_str = input.split("\n\n")

W = {}
for w in wires_str.split("\n"):
    k, v = w.split(': ')
    W[k] = int(v)
print(W)

# AND gates output 1 if both inputs are 1; if either input is 0, these gates output 0.
# OR gates output 1 if one or both inputs is 1; if both inputs are 0, these gates output 0.
# XOR gates output 1 if the inputs are different; if the inputs are the same, these gates output 0.
updated = True
while updated:
    updated = False
    for g in gates_str.split("\n"):
        w1, op, w2, _, t = g.split(' ')
        oldWt = W[t] if t in W else -1
        if w1 in W and w2 in W: 
            if op == 'AND':
                W[t] = W[w1] & W[w2]
            elif op == 'OR':
                W[t] = W[w1] | W[w2]
            elif op == 'XOR':
                W[t] = W[w1] ^ W[w2]

        if t in W and oldWt != W[t]:
            updated = True

print(W)

p1 = ''
OUT = dict(reversed(sorted([(k, v) for k, v in W.items() if k.startswith('z')])))

for k, v in OUT.items():
        p1 += str(v)
print(p1)
p1 = int(p1, 2)
print('p1', p1)
