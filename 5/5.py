#!/usr/bin/env python3
from collections import defaultdict
file1 = '5.in'

R = defaultdict(list)
B = []
rules_complete = False
input = [x.strip() for x in open(file1, 'r').readlines()]
for v in input:
    if len(v.strip()) == 0:
        rules_complete = True
    elif not rules_complete:
        k, v = list(map(int, v.split('|')))
        R[k].append(v)
    elif rules_complete:
        B.append(list(map(int, v.split(','))))

ans1 = 0
ans2 = 0
for b in B:
    valid = True
    # b.reverse()
    for x in range(len(b)):
        # print(b[x])
        for y in R[b[x]]:
            if y in b[0:x]:
                valid = False
                break
    if valid:
        ans1 += b[len(b)//2]
        print(b, "valid", b[len(b)//2])
    else:
        while not valid:
            valid = True
            for x in range(len(b)):
                for y in R[b[x]]:
                    if y in b[0:x]:
                        valid = False
                        old_i = b.index(y)
                        b.insert(x+1, y)
                        b.pop(old_i)
                        break
        ans2 += b[len(b)//2]
        print(b, "fixed", b[len(b)//2])

print(ans1)
print(ans2)