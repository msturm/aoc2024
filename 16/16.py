#!/usr/bin/env python3
from collections import deque
import time
from queue import PriorityQueue
file1 = '16.in'
file1 = '16.test'

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

print(R,C)
for r in range(R):
    for c in range(C):
#        for d, (dr, dc) in enumerate(D):
#            rr = r+dr
#            cc = c+dc
#            if G[r][c] == '.':
#                COST[(r, c, d)] = INF
            if G[r][c] == 'S':
#                if d == 1:
#                    COST[(r, c, d)] = 0
#                else:
#                    COST[(r, c, d)] = INF
                start = (r, c, 1)
            elif G[r][c] == 'E':
#                COST[(r, c, d)] = INF
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
COST = dict()
PQ = PriorityQueue()
PQ.put((0, start[0], start[1], start[2]))
SEEN = set()
counter = 0
#print(COST)
p1_node = (INF,0,0,0)
while not PQ.empty():
    counter += 1
    cur_cost, r, c, d = PQ.get()
#    print(v, node)
    #r, c, d = node 
    if (r, c) == end:
        if p1_node[0] > cur_cost: 
            p1_node = (cur_cost, r, c, d)
        break
    #cur_cost = COST[(r, c, d)]
    for dd, (dr, dc) in enumerate(D):
        rr, cc = r + dr, c + dc
        if dd == d and G[rr][cc] != '#' and (rr, cc, d) not in SEEN: # neighbour in same dir
            SEEN.add((rr, cc, d))
            new_cost = cur_cost + 1
            COST[(rr, cc, d)] = new_cost
            PQ.put((new_cost, rr, cc, d))
#            print('1put', new_cost, cur_cost, rr, cc, d)
        elif (((d-1)%4) == dd or dd == ((d+1)%4)) and G[rr][cc] != '#' and (r, c, dd) not in SEEN: # change of dir
            SEEN.add((r, c, dd))
            new_cost = cur_cost + 1000
            COST[(r, c, dd)] = new_cost
            PQ.put((new_cost, r, c, dd))
#            print('2put', new_cost, r, c, dd)
#            print('cupdate', r, c, new_cost, d)
#    printseen(G, SEEN)
#    printgrid(G, COST)
print('\033[?25h', end="")
p1 = p1_node[0]
print(p1_node)

PQ = PriorityQueue()
COST2 = dict()
PQ.put((0, p1_node[1], p1_node[2], p1_node[3]))
p1_cost = p1_node[0]
SEEN = set()
while not PQ.empty():
    counter += 1
    cur_cost, r, c, d = PQ.get()
#    print(v, node)
    #r, c, d = node 
    if r == start[0] and c == start[1]:
        break
    #cur_cost = COST[(r, c, d)]
    for dd, (dr, dc) in enumerate(D):
         
        rr, cc = r + dr, c + dc
        if (dd-2)%4 == d and G[rr][cc] != '#' and (rr, cc, d) not in SEEN: # neighbour in same dir
            SEEN.add((rr, cc, d))
            new_cost = cur_cost + 1
            COST2[(rr, cc, d)] = new_cost
            PQ.put((new_cost, rr, cc, d))
#            print('1put', new_cost, cur_cost, rr, cc, d)
        elif (((d-1)%4) == dd or dd == ((d+1)%4)) and G[rr][cc] != '#' and (r, c, dd) not in SEEN: # change of dir
            SEEN.add((r, c, dd))
            new_cost = cur_cost + 1000
            COST2[(r, c, (dd-2)%4)] = new_cost
            PQ.put((new_cost, r, c, (dd-2)%4))
        
print('c', COST)
print('c2', COST2)
p2_s = set()
for r in range(R):
    for c in range(C):
        for dir in range(4):
            if (r, c, d) in COST and (r, c, d) in COST2 and COST[(r, c, d)] + COST2[(r, c, d)] == p1_cost:
                p2_s.add((r, c))
                
 
print("print R", p2_s) 
printseen(G, p2_s)
#printgrid(G, COST)
print('p1', p1)
print('p2', len(p2_s))
                
    
