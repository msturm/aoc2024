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
    # get fastest path
    SEEN = set()
    PQ = PriorityQueue()
    PQ.put((COST[optimize_start], optimize_start[0], optimize_start[1]))
    ans = 0
    while not PQ.empty():
        cur_cost, r, c = PQ.get()
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

p1 = 0
p2 = 0
path.reverse()
count = 0
max_cheat_length = 20
min_shortcut_gain = 100 
GROUP = defaultdict(int)
for i1, (r1,c1)  in enumerate(path):
    count += 1
    print(r1, c1, count, 'of', len(path))
    for i2 in range(i1+1, len(path)):
        r2, c2 = path[i2]
        if abs(r2-r1)+abs(c2-c1) ==2:
            shortcut_gain = COST[(r2,c2)] - COST[(r1, c1)] - 2
            if shortcut_gain >= min_shortcut_gain:
                p1+=1
        if abs(r2-r1)+abs(c2-c1) <= max_cheat_length:
            cheat_length = abs(r2-r1)+abs(c2-c1) 
    #        print(r1,c1,r2,c2, cheat_length, COST[(r2,c2)], COST[(r1, c1)])
            if cheat_length <= max_cheat_length: 
                shortcut_gain = COST[(r2,c2)] - COST[(r1, c1)] - cheat_length
                if shortcut_gain >= min_shortcut_gain:
                    GROUP[shortcut_gain] += 1
    #                print('cheat', cheat_length,  shortcut_gain, r1, c1, r2, c2)
                    p2 += 1

print('p1', p1)
print('p2', p2)

print(sum([v for _, v in GROUP.items()]))
