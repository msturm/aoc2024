#!/usr/bin/env python3
from copy import deepcopy

file1 = '3.in'

input = [x.strip() for x in open(file1, 'r').readlines()]
ans1 = 0
ans2 = 0
last_dont = ''
last = ''
val1 = ''
val2 = ''
is_enabled = True
for v in input:
    for c in v:

            if c == 'm' and last == '':
                last = 'm'
                last_dont = ''
            elif c == 'u' and last == 'm':
                last += 'u'
            elif c == 'l' and last == 'mu':
                last += 'l'
            elif c == '(' and last == 'mul':
                last += '('
            elif c.isdigit() and last == 'mul(' and len(val1) < 3:
                val1 += c
            elif c == ',' and last == 'mul(':
                last += ','
            elif c.isdigit() and last == 'mul(,' and len(val2) < 3:
                val2 += c
            elif c == ')' and last == 'mul(,':
                ans1 += int(val1) * int(val2)
                if is_enabled:
                    ans2 += int(val1) * int(val2)
                last_dont = ''
                last = ''
                val1 = ''
                val2 = ''
            # parsing don't
            elif c == 'd' and last_dont == '':
                last = ''
                val1 = ''
                val2 = ''
                last_dont = 'd'
            elif c == 'o' and last_dont == 'd':
                last_dont += 'o'
            elif c == 'n' and last_dont == 'do':
                last_dont += 'n'
            elif c == '\'' and last_dont == 'don':
                last_dont += '\''
            elif c == 't' and last_dont == 'don\'':
                last_dont += 't'
            elif c == '(' and last_dont == 'don\'t':
                last_dont += '('
            elif c == ')' and last_dont == 'don\'t(':
                is_enabled = False
                last_dont = ''
                last = ''
                val1 = ''
                val2 = ''
            elif c == '(' and last_dont == 'do':
                last_dont += '('
            elif c == ')' and last_dont == 'do(':
                is_enabled = True
                last_dont = ''
                val1 = ''
                val2 = ''
                last = ''
            else:
                last_dont = ''
                last = ''
                val1 = ''
                val2 = ''

print(ans1)
print(ans2)