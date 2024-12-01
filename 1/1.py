#!/usr/bin/env python3
from collections import defaultdict
file1 = '1.in'


input = [x.strip() for x in open(file1, 'r').readlines()]
l1, l2 = [], []
l2count = defaultdict(int)
for v in input:
    a, b = v.split('   ')
    l1.append(int(a))
    l2.append(int(b))
    l2count[int(b)] += 1

l1.sort()
l2.sort()
ans1 = 0
ans2 = 0
for x in range(len(l1)):
    ans1 += abs(l2[x] - l1[x])
    ans2 += l1[x]*l2count[l1[x]]

print("ans1: ", ans1)
print("ans2: ", ans2)




