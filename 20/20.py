#!/usr/bin/env python3
import re
from collections import defaultdict
from queue import PriorityQueue
from collections import deque

def nums(v):
	return [int(x) for x in re.findall("\d+",v)]


file1 = '20.in'
#file1 = '20.test'

input = [x.strip() for x in open(file1, 'r').readlines()]

G =[]
D = [(-1,0), (0, 1), (1, 0), (0,-1)]
s = (0, 0)
e = (0, 0)
R = len(input)
C = len(input[0])

for r, v in enumerate(input):
    G.append(v)
    for c in range(len(v)):
        if G[r][c] == 'S':
            s = (r, c)
        if G[r][c] == 'E':
            e = (r, c)

def print_grid(G):
    for r in range(R):
        for c in range(C):
            if (r, c) in fastest:
                print('O', end='')
            else:
                print(G[r][c], end='')
        print("")


print(R, C, s, e)
COST = {s: 0}
def calculate_speed(G, shortcut, target, optimize_start):
#    print('calc_speed', shortcut, target, optimize_start)
    # get fastest path
    SEEN = set()
    PQ = PriorityQueue()
    PQ.put((COST[optimize_start], optimize_start[0], optimize_start[1]))
    ans = 0
    while not PQ.empty():
        cur_cost, r, c = PQ.get()
        #print(cur_cost, r, c)
        if (r, c) == e:
            ans = cur_cost
            if target == 0:
                COST[(r, c)] = cur_cost
            break
        if (r, c) in SEEN:
            continue
        SEEN.add((r, c))
        if target == 0:
            COST[(r, c)] = cur_cost
        for dr, dc in D:
            rr, cc = r+dr, c+dc
            if 0 <= rr < R and 0 <= cc < C:
                if (rr, cc) in shortcut:
                    PQ.put((cur_cost+1, rr, cc))
                elif target > 0 and (rr, cc) in COST and cur_cost + 1 <= COST[(rr, cc)]:
                    PQ.put((cur_cost+1, rr, cc))
                elif G[rr][cc] in ['.', 'E']: 
                    PQ.put((cur_cost+1, rr, cc))

    return ans
#
#    # check if shortcut is actually used
#    if set(shortcut).issubset(set(fastest)):
#        return ans
#    else:
#        return target 

target = calculate_speed(G, [], 0, s)

Q = deque([e])
path = []
while Q:
    r, c = Q.popleft()
    path.append((r, c))
    for dr, dc in D:
        rr, cc = r+dr, c+dc
        if (rr, cc) in COST and COST[(rr, cc)] == COST[(r, c)] -1:
            Q.append((rr, cc))
print("path", path)

def path_through_block(s, e):
    SEEN = set()
    PQ = PriorityQueue()
    PQ.put((0, s[0], s[1]))
    ans = 0
    while not PQ.empty():
        cur_cost, r, c = PQ.get()
        #print(cur_cost, r, c, e)
        if (r, c) == e:
            ans = cur_cost
            break
        if (r, c) in SEEN:
            continue
        SEEN.add((r, c))
        for dr, dc in D:
            rr, cc = r+dr, c+dc
            if 0 <= rr < R and 0 <= cc < C and ((rr, cc) == e or  G[rr][cc] == '#'): 
                PQ.put((cur_cost+1, rr, cc))

    return ans


print(target)
p1 = 0
print("blocktest", path_through_block((1,7),(1,9)), (COST[(1,9)] - COST[(1,7)]))
path.reverse()
count = 0
for i1, (r1,c1)  in enumerate(path):
    count += 1
    print(r1, c1, count, 'of', len(path))
    for i2 in range(i1+1, len(path)):
        r2, c2 = path[i2]
        if abs(r2-r1)+abs(c2-c1) ==2:
#            path_length = path_through_block((r1, c1), (r2, c2))
#            print(r1,c1,r2,c2)

            #if path_length == 2:
            shortcut_gain = COST[(r2,c2)] - COST[(r1, c1)] - 2
            if shortcut_gain >= 100:
                p1+=1


# calculate path
#TEST = defaultdict(int)
#p1 = 0
#for r in range(1,R-1):
#    print('r', r)
#    for c in range(1,C-1):
#        if G[r][c] == '#':
#            # vertical
#
#            # should have at least 2 '.' as neighbour
#            neighbours = 0
#            optimize_start = s 
#            min_cost = target 
#            for dr, dc in D:
#                rr, cc = r+dr, c+dc
#                if G[rr][cc] == '.' or G[rr][cc] == 'E' or G[rr][cc] == 'S':
#                    if (rr, cc) in COST:
##                        print(rr, cc, min_cost, COST[(rr, cc)])
#                        if COST[(rr, cc)] < min_cost:
#                            min_cost = COST[(rr, cc)]
#                            optimize_start = (rr, cc)
#                    neighbours += 1
#
#            if neighbours > 1:
#                shortcut = [(r, c)]
#                new_speed = calculate_speed(G, shortcut, target, optimize_start)
##                print(r,c,new_speed, target-new_speed)
#                if target-new_speed > 0:
#                    TEST[target-new_speed] += 1
#                if target-new_speed >= 100:
#                    p1 += 1
#print(TEST)
#print(sorted([(k, len(v)) for k, v in TEST.items()]))
#print(sorted([(k, v) for k, v in TEST.items()]))
# for p1, faster would be to just measure the length of the start of the shortcut to the end of the shortcut.
print('p1', p1)
#print('p2', p2)
            

#print(fastest)
