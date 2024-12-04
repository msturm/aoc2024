#!/usr/bin/env python3
import re
import copy
from audioop import reverse

file1 = '4.in'

input = [x.strip() for x in open(file1, 'r').readlines()]
G = []
ans1 = 0
for v in input:
    G.append([x for x in v])

offsets = [[(1,0), (2,0), (3,0)],
           [(-1,0), (-2,0), (-3,0)],
           [(0,1), (0,2), (0,3)],
           [(0,-1), (0,-2), (0,-3)],
           [(1,1), (2,2), (3,3)],
           [(-1,-1), (-2,-2), (-3,-3)],
           [(1,-1), (2,-2), (3,-3)],
           [(-1,1), (-2,2), (-3,3)]]


for r in range(len(G)):
    for c in range(len(G[0])):
        if G[r][c] == 'X':
            for o in offsets:
                word = G[r][c]
                for i in range(3):
                    rr = r + o[i][0]
                    cc = c + o[i][1]
                    if rr < 0 or cc < 0 or rr >= len(G) or cc >= len(G[0]):
                        break
                    word += G[rr][cc]
                if word == 'XMAS':
                    ans1 += 1
print(ans1)

ans2 = 0
X = [[(-1,-1),(0, 0),(1, 1)],[(-1, 1),(0, 0),(1,-1)]]

for r in range(len(G)):
    for c in range(len(G[0])):
        if G[r][c] == 'A':
            w1, w2 = '', ''
            for i in range(3):
                rr = r + X[0][i][0]
                cc = c + X[0][i][1]
                rr2 = r + X[1][i][0]
                cc2 = c + X[1][i][1]
                if rr < 0 or cc < 0 or rr >= len(G) or cc >= len(G[0]):
                    break
                if rr2 < 0 or cc2 < 0 or rr2 >= len(G) or cc2 >= len(G[0]):
                    break
                w1 += G[rr][cc]
                w2 += G[rr2][cc2]

            if (w1 == 'MAS' or w1[::-1] == 'MAS') and (w2 == 'MAS' or w2[::-1] == 'MAS'):
                ans2 += 1
print(ans2)