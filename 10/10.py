#!/usr/bin/env python3
file1 = '10.in'
#file1 = '10.test'

input = [x.strip() for x in open(file1, 'r').readlines()]
G = [] 
R = len(input)
C = len(input[0])
for v in input:
   G.append([int(x) for x in v]) 

print(G)

D = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def is_valid(r,c,P,p2=False):
    if G[r][c] == 9:
        if p2:
            return 1
        else:
            return set([(r, c)])  
    else:
        count=0
        for dr, dc in D:
            rr, cc = r+dr, c+dc
            if 0 <= rr < R and 0 <= cc < C:
                if G[rr][cc] == G[r][c] + 1:
                    if p2:
                        count += is_valid(rr, cc, P, p2)          
                    else:
                        P = P.union(is_valid(rr, cc, P, p2))
        if p2:
            return count
        else:
            return P 

p1 = 0
p2 = 0
for r in range(len(G)):
    for c in range(len(G[0])):
        if G[r][c] == 0:
            p1 += len(is_valid(r, c, set()))
            p2 += is_valid(r, c, set(), p2=True)

print(p1)
print(p2)
