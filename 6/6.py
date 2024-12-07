#!/usr/bin/env python3
from copy import deepcopy
from collections import defaultdict
from http.cookiejar import debug

file1 = '6.in'
#file1 = '6.test'


input = [x.strip() for x in open(file1, 'r').readlines()]
SO = {}
si = 0
dir = [(-1,0), (0,1), (1,0), (0,-1)]
sr, sc = 0,0
R, C = len(input), len(input[0])
for r in range(len(input)):
    for c in range(len(input[0])):
        if input[r][c] == '#':
            SO[(r,c)] = '#'
        elif input[r][c] == '^':
            sr, sc = r,c


visited = set()

O = SO
i = si
cr, cc = sr, sc
while True:
    # check for loop

    dr, dc = dir[i]
    if not (0 <= cr < R and 0 <= cc < C): # out of bounds
        break
    elif (cr+dr, cc+dc) in O: #rotate
        i += 1
        if i >= len(dir):
            i = 0
        dr, dc = dir[i]

    visited.add((cr, cc))
    cr, cc = cr+dr, cc+dc
p1 = len(visited)    

# part 2
p2 = 0
#for (nr, nc) in visited:
for nr in range(R):
#    if (nr%10)==0:
#        print(nr, p2)
    for nc in range(C):
        visited_with_d = set()
        i = si 
        cr, cc = sr, sc
        while True:
            if (cr, cc, i) in visited_with_d:
                p2+= 1
                break
            visited_with_d.add((cr, cc, i))
            dr, dc = dir[i]
            if not (0 <= cr < R and 0 <= cc < C): # out of bounds
                break
            elif (cr+dr, cc+dc) in O or cr+dr==nr and cc+dc==nc: #rotate
                i += 1
                if i >= len(dir):
                    i = 0
                dr, dc = dir[i]
            else:
                cr, cc = cr+dr, cc+dc

# for r in range(R):
#   for c in range(C):
#        if (r,c) in positive_obstacles:
#            print('O', end='')
#        elif (r,c) in visited:
#            print('X', end='')
#        elif (r,c) in O:
#            print('#', end='')
#        else:
#            print('.', end='')
#    print("")

print("p1", p1)
print("p2", p2)
