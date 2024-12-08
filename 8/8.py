#!/usr/bin/env python3
file1 = '8.in'

input = [x.strip() for x in open(file1, 'r').readlines()]
A = {} 
R = len(input)
C = len(input[0])
AN1 = {}
AN2 = {}
for r, v in enumerate(input):
    for c,w in enumerate(v):
        if w != '.':
            A[(r,c)] = w

print(A)            

for (r1, c1) in A:
    # find other attenas with same freq:
    for (r2, c2) in A:
        if r2 != r1 and c2 != c1 and A[(r1,c1)] == A[(r2,c2)]:
      #      print("pair", (r1,c1), (r2,c2), A[(r1, c1)])
            AN2[(r1,c1)] = '#'
            AN2[(r2,c2)] = '#'
            rr1 = r1-r2
            rr2 = r2-r1
            cc1 = c1-c2
            cc2 = c2-c1 
            
            n1 = (r1+r1-r2,c1+c1-c2)
            nr1, nc1 = n1
            n2 = (r2+r2-r1,c2+c2-c1)
            nr2, nc2 = n2
            if 0 <= nr1 < R and 0 <= nc1 < C:
                AN1[n1]='#'
            if 0 <= nr2 < R and 0 <= nc2 < C:
                AN1[n2]='#'

            while 0 <= nr1 < R and 0 <= nc1 < C:
                AN2[n1]='#'
                n1 = (nr1+r1-r2,nc1+c1-c2)
                nr1, nc1 = n1
                
            while 0 <= nr2 < R and 0 <= nc2 < C:
                AN2[n2]='#'
                
                n2 = (nr2+r2-r1,nc2+c2-c1)
                nr2, nc2 = n2
print('p1', len(AN1))            
print('p2', len(AN2))            
exit(1)
for r in range(R):
    for c in range(C):
        if (r, c) in A:
            print(A[(r,c)], end='')
        elif (r, c) in AN:
            print('#', end='')
        else: 
            print('.',end='')
    print('') 
