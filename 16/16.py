#!/usr/bin/env python3
from collections import deque
import time
from queue import PriorityQueue
file1 = '16.in'
#file1 = '16.test3'

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
        for d, (dr, dc) in enumerate(D):
            rr = r+dr
            cc = c+dc
            if G[r][c] == '.':
                COST[(r, c, d)] = INF
            elif G[r][c] == 'S':
                if d == 1:
                    COST[(r, c, d)] = 0
                else:
                    COST[(r, c, d)] = INF
                start = (r, c, 1)
            elif G[r][c] == 'E':
                COST[(r, c, d)] = INF
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
PQ = PriorityQueue()
PQ.put((0, start))
SEEN = set()
counter = 0
#print(COST)
while not PQ.empty():
    counter += 1
    v, node = PQ.get()
#    print(v, node)
    r, c, d = node 
    if (r, c) == end:
        continue
    cur_cost = COST[(r, c, d)]
    for dd, (dr, dc) in enumerate(D):
        rr = r + dr
        cc = c + dc
        if dd == d and (rr, cc, d) in COST and (rr, cc, d) not in SEEN: # neighbour in same dir
            SEEN.add((rr, cc, d))
            new_cost = min(COST[(rr, cc, d)], cur_cost + 1)
            COST[(rr, cc, d)] = new_cost
            PQ.put((new_cost, (rr, cc, d)))
#            print('1put', new_cost, cur_cost, rr, cc, d)
        elif (((d-1)%4) == dd or dd == ((d+1)%4)) and (r, c, dd) in COST and (r, c, dd) not in SEEN: # change of dir
            SEEN.add((r, c, dd))
            new_cost = min(COST[(r, c, dd)], cur_cost + 1000)
            COST[(r, c, dd)] = new_cost
            PQ.put((new_cost, (r, c, dd)))
#            print('2put', new_cost, r, c, dd)
#            print('cupdate', r, c, new_cost, d)
#    printseen(G, SEEN)
#    printgrid(G, COST)
print('\033[?25h', end="")
p1 = INF
for d in range(len(D)):
    r, c = end
    print(d, COST[(r, c, d)])
    p1 = min(p1, COST[(r, c, d)])

Q = deque([(end[0], end[1], 0)])
R = set()
while Q:
    print(Q)
    r, c, d = Q.pop()
    R.add((r, c, d))
    for dd, (dr, dc) in enumerate(D):
        rr = r+dr
        cc = c+dc
        if dd == d and (rr, cc, dd) in COST and COST[(rr, cc, dd)] < COST[(r, c, d)]:
            Q.appendleft((rr, cc, dd))
        elif (r, c, dd) in COST and COST[(r, c, dd)] < COST[(r, c, d)]:
            Q.appendleft((r, c, dd))
#            print(r, c, rr, cc, COST[(rr,cc)][1], COST[(r, c)][1], COST[(rr,cc)][0], COST[(r, c)][0])
#                print('yes')
                #Q.appendleft((rr,cc))
                
        
            
            
#printseen(G, R)
#printgrid(G, COST)
print('p1', p1)
print('p2', len(R))
                
    
