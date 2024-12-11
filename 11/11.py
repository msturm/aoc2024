#!/usr/bin/env python3
from collections import deque
file1 = '11.in'
#file1 = '11.test'

input = [x.strip() for x in open(file1, 'r').readlines()]
N = deque()
for v in input:
    for x in v.split():
        N.append(x)

CACHE = {}
def count_items(x, t):
    if (x, t) in CACHE:
        return CACHE[(x, t)]
    if t == 0:
        return 1
    elif x == 0:
        result = count_items(1, t-1)
        CACHE[(x, t)] = result
    elif len(str(x))%2==0:
        str_x = str(x)
        result = count_items(int(str_x[:len(str_x)//2]), t-1) + count_items(int(str_x[len(str_x)//2:]), t-1)   
        CACHE[(x, t)] = result
    else:
        result = count_items(x*2024, t-1)
    CACHE[(x, t)] = result
    return result
    
    
t= 25
p1 = 0
N = [int(x) for x in input[0].split()]
for x in N: 
    p1 += count_items(x, t) 
    #print(count_items(x, t), x, t)
p2 = sum([count_items(x, 75) for x in N])
print("p1", p1)
print("p2", p2)
