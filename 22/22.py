#!/usr/bin/env python3
import re
from collections import defaultdict
from collections import deque

def nums(v):
	return [int(x) for x in re.findall("\d+",v)]

D = [(-1,0), (0, 1), (1, 0), (0,-1)]

file1 = '22.in'
#file1 = '22.test'

def calc_nextnumber(v, steps=1):
    ov = v
    for _ in range(steps):
        nv = ov * 64 
        nv = ov ^ nv
        nv = nv % 16777216
        nv2 = nv // 32
        nv2 = nv ^ nv2
        nv2 = nv2 % 16777216
        nv3 = nv2 * 2048
        nv3 = nv2 ^ nv3
        nv3 = nv3 % 16777216
        ov = nv3
    print(v, ':', nv3)
    return nv3


input = [x.strip() for x in open(file1, 'r').readlines()]
p1 = 0
for v in input:
    p1 += calc_nextnumber(int(v), 2000)
    
print(p1)    
    
    


#Calculate the result of multiplying the secret number by 64. Then, mix this result into the secret number. Finally, prune the secret number.
#Calculate the result of dividing the secret number by 32. Round the result down to the nearest integer. Then, mix this result into the secret number. Finally, prune the secret number.
#Calculate the result of multiplying the secret number by 2048. Then, mix this result into the secret number. Finally, prune the secret number.

#To mix a value into the secret number, calculate the bitwise XOR of the given value and the secret number. Then, the secret number becomes the result of that operation. (If the secret number is 42 and you were to mix 15 into the secret number, the secret number would become 37.)
#To prune the secret number, calculate the value of the secret number modulo 16777216. Then, the secret number becomes the result of that operation. (If the secret number is 100000000 and you were to prune the secret number, the secret number would become 16113920.)
