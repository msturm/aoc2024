#!/usr/bin/env python3
from copy import deepcopy
from collections import defaultdict
from http.cookiejar import debug

file1 = '6.in'

input = [x.strip() for x in open(file1, 'r').readlines()]
O = {}
i = 0 # North
si = i
dir = [(-1,0), (0,1), (1,0), (0,-1)]
cr, cc = 0,0
sr, sc = 0,0
R, C = len(input), len(input[0])
for r in range(len(input)):
    for c in range(len(input[0])):
        if input[r][c] == '#':
            O[(r,c)] = '#'
        elif input[r][c] == '^':
            cr, cc = r,c
            sr, sc = r,c

def has_loop(O):
    cc, cr, i = sc, sr, si
    visited = set()
    visited_with_d = defaultdict(int)
    while 0 <= cr+dir[i][0] < R and 0 <= cc+dir[i][1] < C:
        if cr+dir[i][0] < 0 or cr+dir[i][0] >= R or cc+dir[i][1] < 0 or cc+dir[i][1] >= C: # not a loop, we go out of bounds
            print("not a loop:", cr, cc, i)
            break
        # print(cr, cc, i)
        visited.add((cr, cc))
        visited_with_d[(cr, cc, i)] += 1
        if visited_with_d[(cr, cc, i)] > 1:
            print("loop:", cr, cc, i)
            return True
        if (cr+dir[i][0], cc+dir[i][1]) in O: #rotate
            i += 1
            if i >= len(dir):
                i = 0
        cr, cc = cr+dir[i][0], cc+dir[i][1]
    if (cr, cc, i) in visited_with_d:
        # print(cr, cc, i, visited_with_d)
        return True
    else:
        # print("p1", len(visited))
        return False

p2 = 0
visited = set()
visited_with_d = set()
obstacles_checked = set()
positive_obstacles = set()
while cr >= 0 and cc >= 0 and cr < R and cc < C:
    # check for loop
    if (cr+dir[i][0], cc+dir[i][1]) not in obstacles_checked:
        if 0 <= cr+dir[i][0] < R and 0 <= cc+dir[i][1] < C:
            obstacles_checked.add((cr+dir[i][0], cc+dir[i][1]))
            OC = deepcopy(O)
            OC[(cr+dir[i][0], cc+dir[i][1])] = '#'
            if has_loop(OC):
                p2+=1
                positive_obstacles.add((cr+dir[i][0], cc+dir[i][1]))
                print("loop", cr+dir[i][0], cc+dir[i][1], p2)

    visited.add((cr, cc))
    visited_with_d.add((cr, cc, i))
    if cr+dir[i][0] < 0 or cr+dir[i][0] >= R or cc+dir[i][1] < 0 or cc+dir[i][1] >= C:
        break
    elif (cr+dir[i][0], cc+dir[i][1]) in O: #rotate
        i += 1
        if i >= len(dir):
            i = 0

    # part 1
    cr, cc = cr+dir[i][0], cc+dir[i][1]

    # print(cr, cc)

for r in range(R):
    for c in range(C):
        if (r,c) in positive_obstacles:
            print('O', end='')
        elif (r,c) in visited:
            print('X', end='')
        elif (r,c) in O:
            print('#', end='')
        else:
            print('.', end='')
    print("")
# print(visited)
# has_loop(O)
print(len(visited))
print("p2", p2)
print(positive_obstacles)