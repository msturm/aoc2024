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
for v in input[0:3]:
    R.append(nums(v)[0])

def run_prog(R, P):
    A, B, C = 0, 1, 2
    ip = 0
    out = []

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
#    return ','.join([str(x) for x in out])
    return out



print('p1', ','.join([str(x) for x in run_prog(R, P)]))
        
# 3,0 makes the program jump to A, if A == 0, otherwise exit
# 5,x prints something
# 5,4 prints register A
# 5,5 prints register B
# 5,6 prints register C
# 0,3 A//2**3

# FOR THE TEST PROGRAM
# Lets assume
#0,3,5,4,3,0
# 0,3 A//2**3
# 5,4 print A
# 3,0 if A != 0, exit(0), else pi = 0
# so to print, we first need to make sure A%8 == (val to print) and then to 1

# so to print 0, 3, 5, 4, 3, 0 we need to 0*8+3*8+5*8+4*8+3*8+0*8 = 
# for example, to print 3, A needs to be 3*8 = 24

# if you only want one number, you need to have prime factors for the %8
# To print 0:
# A needs to be (x//8)%8=0
# To print 3:
# A needs to be (x//8)%8=3, so x==24 or x==88 or x==152, etc. 
# 24 prints 3,0
# 88 prints 3,1,0
# 152 prints 3,2,0
# 207 prints 3,3,0
# to print 5
# A needs to be (x//8)%8=5, so x==104 or 168
# so 0,3 should result in A%8=0. 0,3 == A//2**3 = A//8 => A == 0

# To output 2, we should have op 5, x%8=2, which is true for 10, 18, 26, 34, ...
# To output 4, we should have op 5, in order to output 4. To output 0, we should have any x for which  x%8==4, 12,20,28,36, ...
# Let's say we want to output 0,3,5,4,3,0:
# it is unavailable to have a 0 printed at the end, because the last loop will always print 0
# Jump should jump to ip=2, so A should be 2, the value after ip=2 (which is 4) determines what it prints, in this case reg[A]
# In order to print 0, reg[A] should be reg[A]%8=0 
# In order to print 3, jump should go to 2 again

# basically, it is binary, but with 8 instead of 2
# first digit is x*8, second is x*64*64 third is x*64*64*64, etc.
# so 0,3,5,4,3,0 requires:
# 0, 24, 
# 0*8 + 3*8^2 + 5*8^3 + 4*8^4 + 3*8^5

PTEST = [0,3,5,4,3,0]
def calc_p2_test(L):
#    print("calc_p2", L)
    ans = 0
    for n, v in enumerate(L):
        ans += v * 8**(1+n) 
#    print(ans)
    return ans

def exec_program(v):
    R = [v, 0, 0]
    outp = run_prog(R, P)
    return outp

R = [calc_p2_test(PTEST), 0, 0]
target = [2,4,1,5,7,5,1,6,0,3,4,3,5,5,3,0]
start = 8**14 # minimum length is in most cases 8**15 to get 16 digits, but apparently not for my input
power = 13
field_to_check = 15
while field_to_check >= 0:
    start += 8**power 
    result = exec_program(start) 
    if power == 0:
        print(start, result)
    if len(result) == len(target) and result[field_to_check] == target[field_to_check]:
        if power > 1:
            power -= 1
        if field_to_check != 0:
            field_to_check -= 1
        else:
            while not all([x==y for x, y in zip(result, target)]): 
                start -= 1
                result = exec_program(start) 
             #   print(field_to_check, start, power, result)

            field_to_check -= 1
        #print(field_to_check, start, power, result)
p2 = start
print("p2",p2)

    

# FOR THE ACTUAL INPUT
# 2,4,1,5,7,5,1,6,0,3,4,3,5,5,3,0
# from the back
# 3,0 if A != 0, exit(0), else pi = 0
# 5,5 prints register B
# 4,3 B = B XOR C
# 0,3 A=A//8 -- not relevant for the current digit, just shifting A
# 1,6 B=B XOR 6
# 7,5 C=A//2^B
# 1,5 B = B XOR 5
# 2,4 B = A % 8

# to print 3,0:
# B needs to be 3
#B = B XOR C
#B = ((A%8) XOR 5) XOR (A%8)*2**(B XOR 5))

# C needs to be B in order to succeed
# C needs to be 5
# C = A//2**B -> 
# because of B XOR 5, C can only 

# B = B XOR C
# B = B XOR 6
# B = B XOR 5
# B = A % 8

# A = A//8

# it takes 3 bits from A
# 


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
    
