#!/usr/bin/env python3
file1 = '13.in'
#file1 = '13.test'

input = open(file1, 'r').read()

m_input = input.split("\n\n")
machines = []
p1 = 0
p1_fast = 0
p2_fast = 0

def solve(buttons, prize_x, prize_y, p2=False):
    # see https://flexbooks.ck12.org/cbook/ck-12-college-precalculus/section/10.2/primary/lesson/systems-of-two-equations-and-two-unknowns-c-precalc/ 
    # and https://www.reddit.com/r/adventofcode/comments/1hd5b6o/comment/m1ub740/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
    # to undertand this... basically, I'm solving (1st example) 94x+22y = 8400 and 34x + 67y = 5400 -> 6298x = 562800 and -748x = -118800 -> 5550x=444000 -> x = 80
    # and then fill it in to get y (= button B presses)
    # for part 2, just first add 1 trillion to prize_x and prize_y
    tokens = 0
    f_valid = False
    if p2:
        prize_x = prize_x + 10000000000000
        prize_y = prize_y + 10000000000000

    ix = buttons[0][1] * buttons[1][0]
    iy = buttons[0][0] * buttons[1][1]
    iprizex = prize_x * buttons[1][1]
    iprizey = prize_y * buttons[1][0] 
    a_press = (iprizex-iprizey)//(-ix+iy)
    b_press = (prize_x - (buttons[0][0] * a_press))//buttons[1][0]
    if (prize_x - (buttons[0][0] * a_press)) % buttons[1][0] == 0:
        b_press = (prize_x - (buttons[0][0] * a_press))//buttons[1][0]
        if prize_y - (buttons[0][1] * a_press) - (buttons[1][1] * b_press) == 0:
            f_valid = True
            tokens += a_press*3 + b_press
        
    print('a_press fast', a_press, 'b_press fast', b_press, 'valid', f_valid, 'tokens', a_press*3 + b_press, p1_fast )
    return tokens 


for v in m_input:
    lines = v.split("\n") 
    buttons = []
    prize_x, prize_y = 0,0 
    for i in [0, 1]:
        xstr, ystr = lines[i].split(':')[1].split(',')
        x = int(xstr[2:])
        y = int(ystr[2:])
        buttons.append((x, y))
    xstr, ystr = lines[2].split(':')[1].split(',')
    prize_x = int(xstr[3:])
    prize_y = int(ystr[3:])
    print(buttons, prize_x, prize_y) 
    
# attempt 1 on part 1
#    max_b = max(prize_x//buttons[1][0], prize_y//buttons[1][1])
#    max_b = min(100, max_b)
#    tokens = -1
#    b_press = 0
#    a_press = 0
#    for t in range(100):
#        t += 1
#        b_press = max(0, max_b - t)
#        a_press = 0 
#        valid = False
##        print(a_press, b_press)
#        dx = prize_x - (buttons[1][0]*b_press)
#        dy = prize_y - (buttons[1][1]*b_press)
#        if dx % buttons[0][0] == 0 and dy % buttons[0][1] == 0:
#            a_press = dx//buttons[0][0]
#            if dx - (a_press*buttons[0][0]) == 0 and dy - (a_press * buttons[0][1]) == 0 and 0 <= a_press <=100:
#                valid = True
#                new_tokens = a_press * 3 + b_press
#                print("presses", a_press, b_press, new_tokens, tokens)
#                if tokens == -1 or new_tokens < tokens:
#                    tokens = new_tokens
#    if tokens > -1:
#        p1 += tokens
#        print(tokens)
    p1_fast += solve(buttons, prize_x, prize_y)
    p2_fast += solve(buttons, prize_x, prize_y, p2=True)
#print("p1", p1)

print('p1_fast', p1_fast)
print('p2_fast', p2_fast)
    
        
