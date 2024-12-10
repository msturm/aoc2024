#!/usr/bin/env python3
file1 = '9.in'
#file1 = '9.test'
from copy import deepcopy
from collections import deque
input = [x.strip() for x in open(file1, 'r').readlines()][0]
# input = '12345'
#input = '2333133121414131402'

block_end = len(input) - 1
if block_end % 2 > 0:
    block_end -= 1

while input[block_end] == 0:
    block_end -= 2        

p1 = 0
pointer_block_end = int(input[block_end]) 
print(pointer_block_end)
pointer = 0
current_block = 0
while block_end > current_block:
    block_length = int(input[current_block])
    if current_block%2==0: # even, so 'value'
        value = current_block // 2
        for x in range(block_length):
#            print('n', pointer, 'x', value, '=', pointer*value)
            p1 += pointer * value  
            pointer += 1
    else:       # odd, so empty        
        for x in range(block_length):
            if block_end > current_block:
                value = block_end // 2
#                print('bf', pointer, 'x', value, '=', pointer*value, block_end, pointer_block_end)
                p1 += pointer * value
                pointer_block_end -= 1
                if pointer_block_end == 0:
                    block_end -= 2
                    pointer_block_end = int(input[block_end])
                pointer += 1
                
    current_block += 1

if pointer_block_end > 0 and pointer_block_end < int(input[block_end]):
    while pointer_block_end > 0:
        value = block_end // 2
        print('wrap up', pointer, 'x', value, '=', pointer*value, block_end, pointer_block_end)
        p1 += pointer * value
        pointer_block_end -= 1
        pointer += 1
    
print("p1", p1)
print("p1 pointer", pointer)
print('part2')
# part 2
FS = deque() 
ES = {} 
pointer = 0
A = deque()
FREE = deque() 
for i, s in enumerate(input):
    if i%2 == 0: # file                
        FS.append((pointer, int(s), i//2))
        A.append((pointer, int(s), i//2))
    else: # empty
        FS.append((pointer, int(s), '.'))
        FREE.append((pointer, int(s)))
    pointer += int(s)

# print it
def print_mem(FS):
    for n in range(len(FS)):
        i, s, v = FS[n]
        for m in range(s):
            print(v, end='')
    print("")


NFS = deepcopy(FS)
FINAL = {}
while len(A) > 0:
    file_start, file_length, file_value = A.pop()
#    print(file_start, file_length, file_value)
#    print(FREE)
    moved = False
    for free_index, (free_start, free_length) in enumerate(FREE): 
        if free_start < file_start: # should only move to left
            if free_length >= file_length: 
#                print(file_value, "fits (with margin)", "length:", file_length, "location", free, "freeup", free_length, file_length, free_length - file_length)
                FREE[free_index] = (free_start + file_length, free_length - file_length)
                FINAL[free_start] = (free_start, file_length, file_value)
                moved = True
                break
    if not moved:
#        print(file_value, "not moved", "stays", file_start, file_length)
        FINAL[file_start] = (file_start, file_length, file_value)

#print(FINAL)
p = 0
p2 = 0
while len(FINAL) > 0:
    if p in FINAL:
        s, l, v = FINAL.pop(p)
#        print('final pos', s, 'length', l, 'value', v)
        while l > 0:
            print(v, end='')
            p2 += p * v
            p += 1
            l -= 1
    else:
        print('.', end='')
        p += 1

print('')                    
print("p2", p2)
print("p2 pointer", p)
# print it
#print_mem(NFS)

