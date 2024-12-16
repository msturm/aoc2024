#!/usr/bin/env python3
from collections import deque
import time
from queue import PriorityQueue
file1 = '16.in'
#file1 = '16.test2'

#input = [x.strip() for x in open(file1, 'r').readlines()]
input = open(file1, 'r').read().strip()
G = input.split("\n") 
R = len(G)
C = len(G[0])
D = [(-1,0), (0, 1), (1, 0), (0,-1)]
COST = dict()
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

print(R,C)
for r in range(R):
    for c in range(C):
        for d in range(len(D)):
            if G[r][c] == '.':
                COST[(r, c)] = (INF, 1)
            elif G[r][c] == 'S':
                COST[(r, c)] = (0, 1)
                start = (r, c, 1)
            elif G[r][c] == 'E':
                COST[(r, c)] = (INF, 1)
                end = (r,c)

def printgrid(G, COST):
    for r in range(len(G)):
        for c in range(len(G[0])):
            if (r, c) in COST and COST[(r, c)][0] < INF:
                print(COST[(r, c)][0], end=" ")
            else:
                print(G[r][c], end=" ")
        print("") 
#        print("") 
            
    print("")

def printseen(G, SEEN):
    print(bcolors.CLEAR, end ="")
    for r in range(len(G)):
        for c in range(len(G[0])):
            if (r, c) in SEEN:
                print('*', end="")
            else:
                print(G[r][c], end="")
        print("") 
#        print("") 
            
    print("")
    time.sleep(0.2)



print('\033c')
print('\033[?25l', end="")
#Q = deque([start])
PQ = PriorityQueue()
PQ.put((0, start))
SEEN = set()
counter = 0
while not PQ.empty():
    counter += 1
#    print("queue", PQ)
    _, node = PQ.get()
    print(node)
    r, c, d = node 
    print(r, c)
    SEEN.add((r, c))
    cur_cost, cur_dir = COST[(r, c)]
    for di, (dr, dc) in enumerate(D):
        rr = r + dr
        cc = c + dc
        if (rr, cc) in COST and (rr, cc) not in SEEN:
            new_cost = (0, 0)
            if cur_dir == di:
                new_cost = (cur_cost + 1, di)
            else:
                new_cost = (cur_cost + 1001, di)
            COST[(rr, cc)] = new_cost
            PQ.put((new_cost, (rr, cc, di)))
            print('cupdate', r, c, new_cost, d)
#    printseen(G, SEEN)
#    printgrid(G, COST)
print('\033[?25h', end="")
print(COST)
print(COST[end])
                
    
