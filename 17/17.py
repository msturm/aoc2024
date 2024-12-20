#!/usr/bin/env python3
import re
file1 = '17.in'
#file1 = '17.test'
def nums(v):
   return [int(x) for x in re.findall("\d+", v)]

input = [x.strip() for x in open(file1, 'r').readlines()]
R = [] #registers
print(input[4])
P = nums(input[4]) #program
A, B, C = 0, 1, 2
ip = 0
out = []
for v in input[0:3]:
    R.append(nums(v)[0])

while ip < len(P):
    op = P[ip+1]
    if P[ip] == 0:    # adv
        if op <= 3:
            R[A] = R[A]//(2**op)
        else:
            reg = op-4 
            R[A] = R[A]//(2**R[reg])
    elif P[ip] == 1:   # bxl 
        R[B] = R[B] ^ op
    elif P[ip] == 2:   # bst 
        if op <= 3:
            R[B] = op % 8
        else:
            reg = op - 4
            R[B] = R[reg] % 8 
    elif P[ip] == 3:   # jnz 
        if R[A] > 0:
            ip = op
            continue
    elif P[ip] == 4:   # bxc 
        R[B] = R[B] ^ R[C]
    elif P[ip] == 5:   # out 
        if op <= 3:
            out.append(op%8)
        else:
            reg = op - 4
            out.append(R[reg]%8)
    elif P[ip] == 6:   # bdv 
        if op <= 3:
            R[B] = R[A]//(2**op)
        else:
            reg = op-4 
            R[B] = R[A]//(2**R[reg])
    elif P[ip] == 7:   # cdv 
        if op <= 3:
            R[C] = R[A]//(2**op)
        else:
            reg = op-4 
            R[C] = R[A]//(2**R[reg])
    ip += 2

print('p1', ','.join([str(x) for x in out]))
print('registers', R)
#Combo operands 0 through 3 represent literal values 0 through 3.
#Combo operand 4 represents the value of register A.
#Combo operand 5 represents the value of register B.
#Combo operand 6 represents the value of register C.
#Combo operand 7 is reserved and will not appear in valid programs.
#The adv instruction (opcode 0) performs division. The numerator is the value in the A register. The denominator is found by raising 2 to the power of the instruction's combo operand. (So, an operand of 2 would divide A by 4 (2^2); an operand of 5 would divide A by 2^B.) The result of the division operation is truncated to an integer and then written to the A register.
#
#The bxl instruction (opcode 1) calculates the bitwise XOR of register B and the instruction's literal operand, then stores the result in register B.
#
#The bst instruction (opcode 2) calculates the value of its combo operand modulo 8 (thereby keeping only its lowest 3 bits), then writes that value to the B register.
#
#The jnz instruction (opcode 3) does nothing if the A register is 0. However, if the A register is not zero, it jumps by setting the instruction pointer to the value of its literal operand; if this instruction jumps, the instruction pointer is not increased by 2 after this instruction.
#
#The bxc instruction (opcode 4) calculates the bitwise XOR of register B and register C, then stores the result in register B. (For legacy reasons, this instruction reads an operand but ignores it.)
#
#The out instruction (opcode 5) calculates the value of its combo operand modulo 8, then outputs that value. (If a program outputs multiple values, they are separated by commas.)
#
#The bdv instruction (opcode 6) works exactly like the adv instruction except that the result is stored in the B register. (The numerator is still read from the A register.)
#
#The cdv instruction (opcode 7) works exactly like the adv instruction except that the result is stored in the C register. (The numerator is still read from the A register.)   
    
