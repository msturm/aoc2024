#!/usr/bin/env python3 
from copy import deepcopy

file1 = '7.in' 

input = [x.strip() for x in open(file1, 'r').readlines()]
p1 = 0
p2 = 0

def is_valid(target, r, p1=True):
    if len(r)==1:
        if target == r[0]:
            return True
        else:
            return False
    if is_valid(target, [r[0]+r[1]] + r[2:], p1):
        return True
    if is_valid(target, [r[0]*r[1]] + r[2:], p1):
        return True
    if not p1 and is_valid(target, [int(str(r[0])+str(r[1]))] + r[2:], p1):
        return True
    return False

for v in input:
    t, p = v.split(':')
    t = int(t)
    P = [int(x) for x in p.split()]
    if is_valid(t, P, True):
        p1 += t
    if is_valid(t, P, False):
        p2 += t 
 
print("p1", p1)           
print("p2", p2)           
    

