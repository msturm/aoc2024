#!/usr/bin/env python3
from collections import deque
import time
from queue import PriorityQueue
file1 = '16.in'
#file1 = '16.test'

#input = [x.strip() for x in open(file1, 'r').readlines()]
input = open(file1, 'r').read().strip()
G = input.split("\n") 
R = len(G)
C = len(G[0])
D = [(-1,0), (0, 1), (1, 0), (0,-1)]
start = (0, 0, 1)
end = (0, 0)
INF = 1e12

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[91m'
    FAIL = '\033[93m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    CLEAR = '\033[H'

for r in range(R):
    for c in range(C):
            if G[r][c] == 'S':
                start = (r, c, 1)
            elif G[r][c] == 'E':
                end = (r,c)

#def printgrid(G, COST):
#    for r in range(len(G)):
#        for c in range(len(G[0])):
#            if (r, c) in COST and COST[(r, c)][0] < INF:
#                print(COST[(r, c)][0], end=" ")
#            else:
#                print(G[r][c], end=" ")
#        print("") 
#        print("") 
            
    print("")

def printseen(G, SEEN):
    #print(bcolors.CLEAR, end ="")
    for r in range(len(G)):
        for c in range(len(G[0])):
            if (r, c) in SEEN:
                print('*', end="")
            else:
                print(G[r][c], end="")
        print("") 
            
    print("")
    time.sleep(0.2)



print('\033c')
print('\033[?25l', end="")
COST = dict()
PQ = PriorityQueue()
PQ.put((0, start[0], start[1], start[2]))
SEEN = set()
p1_node = (INF,0,0,0)
while not PQ.empty():
    cur_cost, r, c, d = PQ.get()
#    print(cur_cost, r, c, d)
    if (r, c) == end:
        if p1_node[0] > cur_cost: 
            p1_node = (cur_cost, r, c, d)
#        break
    if (r, c, d) not in COST:
        COST[(r, c, d)] = cur_cost
    if (r, c, d) in SEEN:
        continue
    SEEN.add((r, c, d))
    dr, dc = D[d]
    rr, cc = r + dr, c + dc
    if G[rr][cc] != '#':
        new_cost = cur_cost + 1
        PQ.put((new_cost, rr, cc, d))
    new_cost = cur_cost + 1000
    PQ.put((new_cost, r, c, (d+1)%4))
    PQ.put((new_cost, r, c, (d-1)%4))

print('\033[?25h', end="")
p1 = p1_node[0]
print(p1_node)

COST2 = dict()
PQ = PriorityQueue()
for di in range(len(D)):
    PQ.put((0, end[0], end[1], di))
SEEN = set()
while not PQ.empty():
    cur_cost, r, c, d = PQ.get()
#    print(cur_cost, r, c, d)
#    if (r, c) == (start[0], start[1]):
#        break
    if (r, c, d) not in COST2:
        COST2[(r, c, d)] = cur_cost
    if (r, c, d) in SEEN:
        continue
    SEEN.add((r, c, d))
    dr, dc = D[(d-2)%4]
    rr, cc = r + dr, c + dc
    if G[rr][cc] != '#': 
        new_cost = cur_cost + 1
        print('adding', rr,cc,d, new_cost)
        PQ.put((new_cost, rr, cc, d))
    new_cost = cur_cost + 1000
    PQ.put((new_cost, r, c, (d+1)%4))
    PQ.put((new_cost, r, c, (d-1)%4))

print("cost", COST)
print("")
print("cost2", COST2)

p1_cost = p1_node[0]
p2_s = set()
for r in range(R):
    for c in range(C):
        for d in range(4):
            if (r, c, d) in COST and (r, c, d) in COST2:
                print(r, c, d, COST[(r, c, d)], COST2[(r, c, d)], p1_cost)
            if (r, c, d) in COST and (r, c, d) in COST2 and COST[(r, c, d)] + COST2[(r, c, d)] == p1_cost:
                p2_s.add((r, c))
                
 
printseen(G, p2_s)
#printgrid(G, COST)
print('p1', p1)
print('p2', len(p2_s))
print(p2_s)
                
    
