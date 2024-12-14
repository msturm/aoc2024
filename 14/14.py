#!/usr/bin/env python3
from copy import deepcopy
file1 = '14.in'
#file1 = '14.test'

input = [x.strip() for x in open(file1, 'r').readlines()]
robots = [] 
directions = [] 
N = []
R = 103
C = 101

def print_picture(N, s):
    D = set(N)
    print('s', s, "\n") 
    for r in range(R):
        for c in range(C):
            if (r, c) in D:
                print('#', end='')
            else:
                print('.', end='')
        print('')    
    print('')

#R = 7
#C = 11
picture_count = 0
for v in input:
    p, v = v.split(' ')
    c, r = [int(x) for x in p[2:].split(',')]
    robots.append((r, c))
    c, r = [int(x) for x in v[2:].split(',')]
    directions.append((r, c))
N = deepcopy(robots)
for t in range(20000):
    NN = []
    for i, cur in enumerate(N):
        r, c = cur
        dr, dc = directions[i]
        rr = (r + dr) % R
        cc = (c + dc) % C
        NN.append((rr, cc))
    N = NN
    # i see a picture at 7846 (but that is 7847 seconds)
    if 7830 < t < 7860: 
        picture_count += 1
        print_picture(N, t)
    
   # print(t, N)  
        
q1 = [(0,0),(((R-1)//2), ((C-1)//2))]
q2 = [(0, (((C-1)//2)+1)), (((R-1)//2),C)]
q3 = [(((R-1)//2)+1,0), (R,((C-1)//2))]
q4 = [(((R-1)//2)+1,(((C-1)//2)+1)), (R, C)]
#print(q1, q2, q3, q4)
Q = [q1, q2, q3, q4]
p1 = 1
for q in Q:
    minr, minc = q[0]
    maxr, maxc = q[1]
    qcount = 0
    for n in NN:
        r, c = n
        if minr <= r < maxr and minc <= c < maxc:
            qcount += 1
    p1 *= qcount

print(p1) 
    

