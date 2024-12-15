#!/usr/bin/env python3
import os
import time
from copy import deepcopy
file1 = '15.in'
#file1 = '15.test'

#input = [x.strip() for x in open(file1, 'r').readlines()]
input = open(file1, 'r').read()

grid, moves = input.split("\n\n")
grid = grid.split("\n")

G = dict()
R = len(grid)
C = len(grid[0])
robot = (0,0)
D = [(-1,0), (0, 1), (1, 0), (0,-1)]
Dt = {'^':(-1,0), '>':(0, 1), 'v':(1, 0), '<':(0,-1)}

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

def calculate_G(grid):
    G = dict()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '#':
                G[(r, c)] = '#'
            elif grid[r][c] == 'O':
                G[(r, c)] = 'O'
            elif grid[r][c] == '[':
                G[(r, c)] = '['
            elif grid[r][c] == ']':
                G[(r, c)] = ']'
            elif grid[r][c] == '@':
                G[(r, c)] = '@'
                robot = (r, c)
    return G, robot
    
def calculate_p2_grid(grid):
    p2grid = []
    for l in grid:
        newline = ""
        for v in l:
            if v=='#':
                newline += '##'
            if v=='O':
                newline += '[]'
            if v=='.':
                newline += '..'
            if v=='@':
                newline += '@.'
        p2grid.append(newline)
    return p2grid
        
def move(r, c, robot, d, G):
#    if (r, c) in G:
#        print('move', r, c, robot, d, G[(r, c)])
#    else: 
#        print('move', r, c, robot, d, '.')
    dr, dc = Dt[d]
    rr = r + dr
    cc = c + dc
    if (r, c) not in G or G[(r, c)] == '#':
        return G, robot

    if G[(r, c)] == '[' and d in ['v','^']:
        NEW_G = deepcopy(G)
        NEW_G, robot = move(rr, cc, robot, d, NEW_G)
        NEW_G, robot = move(rr, cc+1, robot, d, NEW_G)
        if (rr, cc) not in NEW_G and (rr, cc+1) not in NEW_G:
            v = NEW_G.pop((r, c))
            NEW_G[rr, cc] = v 
            v = NEW_G.pop((r, c+1))
            NEW_G[rr, cc+1] = v
            return NEW_G, robot
    elif G[(r, c)] == ']' and d in ['v','^']:
        NEW_G = deepcopy(G)
        NEW_G, robot = move(rr, cc, robot, d, NEW_G)
        NEW_G, robot = move(rr, cc-1, robot, d, NEW_G)
        if (rr, cc) not in NEW_G and (rr, cc-1) not in NEW_G:
            v = NEW_G.pop((r, c))
            NEW_G[rr, cc] = v 
            v = NEW_G.pop((r, c-1))
            NEW_G[rr, cc-1] = v
            return NEW_G, robot
    else:
        G, robot = move(rr, cc, robot, d, G)
        if (rr, cc) not in G:
                v = G.pop((r, c))
                G[rr, cc] = v 
                if v == '@':
                    robot = (rr, cc)

#    if d in ['v','^'] and (r,c) in G and G[(r, c)] in ['[',']']:
#        if (r, c) in G and G[(r, c)] == '[' and (rr, cc) not in G and (rr, cc+1) not in G:
#            v = G.pop((r, c))
#            G[rr, cc] = v 
#            v = G.pop((r, c+1))
#            G[rr, cc+1] = v
#        elif (r, c) in G and G[(r, c)] == ']' and (rr, cc) not in G and (rr, cc-1) not in G:
#            v = G.pop((r, c))
#            G[rr, cc] = v 
#            v = G.pop((r, c-1))
#            G[rr, cc-1] = v
#    elif (rr, cc) not in G:
#        v = G.pop((r, c))
#        G[rr, cc] = v 
#        if v == '@':
#            robot = (rr, cc) 
#    if (r, c) in G and G[(r,c)] == '@' and (rr,cc) in G:
#        return orig_G, robot
    return G, robot   

def printgrid(G, m='', step = 0, moves=[]):
    #os.system('clear')
    print(bcolors.CLEAR)
    for r in range(R):
        for c in range(C):
            if (r, c) in G:
                if G[(r,c)] == '@':
                    print(bcolors.BOLD + bcolors.OKBLUE +  G[(r, c)] + bcolors.ENDC,end='')
                elif G[(r,c)] == '#':
                    print(bcolors.BOLD + bcolors.WARNING +  G[(r, c)] + bcolors.ENDC,end='')
                elif G[(r,c)] in ['O','[',']']:
                    print(bcolors.BOLD + bcolors.OKCYAN + G[(r, c)] + bcolors.ENDC,end='')
                else:
                    print(G[(r, c)], end='')
            else:
                print('.', end='')
        print('')
    print('')
    print(bcolors.BOLD + 'current step:' + bcolors.ENDC, moves[step:step+1])
    print(bcolors.BOLD + 'number of steps:' + bcolors.ENDC, step, 'of', str(len(moves)))
    print(str(moves[max(0,step-10):step]) + bcolors.BOLD + bcolors.OKGREEN + str(moves[step:step+1]) + bcolors.ENDC + str(moves[step+1:max(step+10,10)]))
                   
    #time.sleep(0.1)

moves = ''.join(moves.split("\n"))
G, robot = calculate_G(grid)

for m in moves:
    G, robot = move(robot[0], robot[1], robot, m, G)
#printgrid(G) 

# The GPS coordinate of a box is equal to 100 times its distance from the top edge of the map plus its distance from the left edge of the map.
p1 = 0
p2 = 0
for (r, c), v in G.items():
    if v == 'O':
        gps = r * 100 + c
        p1 += gps

# part 2
print('\033c')
print('\033[?25l', end="")

C = C*2
p2grid = calculate_p2_grid(grid)
G, robot = calculate_G(p2grid)

#[print(''.join(x)) for x in p2grid]
c = 0
for m in moves:
    c += 1
#    if c > 65:
#        break
    G, robot = move(robot[0], robot[1], robot, m, G)
#    if c > 461:
#        printgrid(G, m, c, moves)
#    print('step',c)
    printgrid(G, m, c, moves)
printgrid(G)

for (r, c), v in G.items():
    if v == '[':
        gps = r * 100 + c
        p2 += gps
print('p1', p1)
print('p2',p2)
print('\033[?25h', end="")
