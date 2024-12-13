#!/usr/bin/env python3
from collections import deque
from collections import defaultdict
file1 = '12.in'
#file1 = '12.test'


input = [x.strip() for x in open(file1, 'r').readlines()]
G = []
R = len(input)
C = len(input[0])
for v in input:
    G.append(v)

D = [(-1,0), (0, 1), (1, 0), (0, -1)]
FENCES = {}

def count_fence(r, c):
    sides = 4
    if (r, c) in FENCES:
       return FENCES[(r, c)]

    for dr, dc in D:
        rr = r + dr
        cc = c + dc
        if 0 <= rr < R and 0 <= cc < C:
            if G[rr][cc] == G[r][c] and (rr, cc) not in FENCES:
                s = count_fence(rr, cc)
                sides -= 1 + s
    FENCES[(r, c)] = sides
    return sides 


SEEN=set()
p1 = 0
p2 = 0
for r in range(R):
    for c in range(C):
        count = 0
        side = 0
        if (r, c) in SEEN:
            continue
        Q = deque([(r, c)])
        borders = dict()
        while Q:
            r2, c2 = Q.popleft()
            if (r2, c2) in SEEN:
                continue
            SEEN.add((r2, c2))
            count += 1
            for dr, dc in D:
                rr = r2 + dr
                cc = c2 + dc
                if 0 <= rr < R and 0 <= cc < C and G[rr][cc]==G[r2][c2]:
                    Q.append((rr, cc))
                else:
                    if (dr, dc) not in borders: 
                        borders[(dr, dc)] = set()
                    borders[(dr, dc)].add((r2, c2))
                    side += 1
        
        p2sides = 0
        print(borders)
        for i, a in borders.items():
            BORDER_SEEN = set()
            for (pr, pc) in a:
                if (pr, pc) not in BORDER_SEEN:
                    p2sides += 1
                    BORDER_Q = deque([(pr, pc)])
                    while BORDER_Q:
                        r6, c6 = BORDER_Q.popleft()
                        if (r6, c6) in BORDER_SEEN:
                            continue
                        BORDER_SEEN.add((r6, c6))
                        for dr, dc in D:
                            rr = r6 + dr
                            cc = c6 + dc
                            if (rr, cc) in a:
                                BORDER_Q.append((rr, cc))                        
                      

        print(p2sides, G[r][c])   
                                        
        p2 += count * p2sides     
        p1 += count * side 
print("p1",p1)
print("p2",p2)
#for r in range(len(G)):
#    for c in range(len(G[0])):

        
            

