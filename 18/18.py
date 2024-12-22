#!/usr/bin/env python3
from collections import deque
from queue import PriorityQueue
file1 = '18.in'
#file1 = '18.test'

B = [] 
input = [x.strip() for x in open(file1, 'r').readlines()]
D = [(-1,0), (0, 1), (1, 0), (0,-1)]

for v in input:
    x, y = [int(x) for x in v.split(',')]
    B.append((y, x))
    
#print(B)
R, C = 71, 71
#R, C = 7, 7 
# 0-70 vertical/horizontal
# sample 0-6

count = 1024
p1 = 0
p2 = 0
ans = 1
while ans > 0: 
    if count == 1024:
#    if count == 12:
        p1 = ans
    ans = 0
    count += 1
    A = B[0:count]
    p2 = (A[-1][1],A[-1][0])
    A = set(A)
#    print(A)
    print(count)                
    SEEN = set()
    PQ = PriorityQueue()
    PQ.put((0, 0,0))
    while not PQ.empty():
        cur_cost, r, c = PQ.get()
    #    print(cur_cost, r, c)
        if (r, c) == (R-1, C-1):
            ans = cur_cost
            break
        if (r, c) in SEEN:
            continue
        SEEN.add((r, c))
        for dr, dc in D:
            rr, cc = r+dr, c+dc
            if 0 <= rr < R and 0 <= cc < C:
                if (rr, cc) not in A:
                    PQ.put((cur_cost+1, rr, cc))

print('p1', p1)
print('p2', p2)

#for r in range(R):
#    for c in range(C):
#        if (r, c) in A:
#            print('#', end='')
#        else:
#            print('.', end ='')
#    print("")

