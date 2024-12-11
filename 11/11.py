#!/usr/bin/env python3
from collections import deque
file1 = '11.in'
#file1 = '11.test'

input = [x.strip() for x in open(file1, 'r').readlines()]
N = deque()
for v in input:
    for x in v.split():
        N.append(x)


for x in range(25):
    NN = deque()
    for _ in range(len(N)):
        n = N.pop() 
        if n == '0':
            NN.appendleft('1') 
        elif len(n)%2 == 0: # odd number
            NN.appendleft(str(int(n[len(n)//2:])))
            NN.appendleft(str(int(n[0:len(n)//2])))
        else:
            NN.appendleft(str(int(n) * 2024))
    N = NN
    print(N)

p1 = len(N)
print("p1", p1)
