#!/usr/bin/env python3
import re
from collections import defaultdict
from collections import deque
from itertools import combinations

def nums(v):
	return [int(x) for x in re.findall("\d+",v)]

D = [(-1,0), (0, 1), (1, 0), (0,-1)]

file1 = '23.in'
#file1 = '23.test'

conns = defaultdict(list)

input = [x.strip() for x in open(file1, 'r').readlines()]
for v in input:
    node1, node2 = v.split('-')
    conns[node1].append(node2)
    conns[node2].append(node1)
        
print(conns)
clusters = set() 
for n, nodes in conns.items():
    for v,w in combinations(nodes, 2):
        if v in conns[w]:
            clusters.add(tuple(sorted([n, v, w])))
print("\n".join([str(x) for x in clusters]))
p1 = 0
for a, b, c in clusters:
    if a[0] == 't' or b[0] == 't' or c[0] == 't':
        p1 +=1

print('p1', p1)
        
    
    
    
