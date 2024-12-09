#!/usr/bin/env python3
file1 = '9.in'
#file1 = '9.test'
#input = [x.strip() for x in open(file1, 'r').readlines()][0]
input = '123'
block_end = len(input) - 1
if block_end % 2 > 0:
    block_end -= 1
p1 = 0
pointer_block_end = int(block_end) 
pointer = 0
current_block = 0
while block_end >= current_block:
    block_length = int(input[current_block])
    if current_block%2==0: # even, so 'value'
        value = current_block//2
        for x in range(block_length):
            print(pointer, value)
            p1 += pointer * value  
            pointer += 1
    else:       # odd, so empty        
        for x in range(block_length):
            value = 
            p1 += pointer * 
    current_block += 1
            
print(p1)


