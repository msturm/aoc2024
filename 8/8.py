#!/usr/bin/env python3
file1 = '8.in'

input = [x.strip() for x in open(file1, 'r').readlines()]
A = {} 
R = len(input)
C = len(input[0])
AN = {}
for r, v in enumerate(input):
    for c,w in enumerate(v):
        if w != '.':
            A[(r,c)] = w

print(A)            

for (r1, c1) in A:
    # find other attenas with same freq:
    for (r2, c2) in A:
        if r2 != r1 and c2 != c1 and A[(r1,c1)] == A[(r2,c2)]:
            n1 = (r1+r1-r2,c1+c1-c2)
            n2 = (r2+r2-r1,c2+c2-c1)
            nr1, nc1 = n1
            nr2, nc2 = n2
            print("pair", (r1,c1), (r2,c2), A[(r1, c1)])
            if 0 <= nr1 < R and 0 <= nc1 < C:
                print('antidote', n1)
                AN[n1]='#'
            if 0 <= nr2 < R and 0 <= nc2 < C:
                print('antidote', n2)
                AN[n2]='#'
print(len(AN))            
