#!/usr/bin/env python3
from collections import defaultdict
import copy
file1 = '2.in'

input = [x.strip() for x in open(file1, 'r').readlines()]
reports = []
rv = defaultdict(bool)
for v in input:
    reports.append([int(x) for x in v.split()])

def check_report(r, fixattempt = 0):
    report = copy.deepcopy(r)
    if report[0] > report[1]:
        report.reverse()

    for y in range(len(report)):
        if y >= 1:
            if report[y-1] >= report[y] or report[y]-report[y-1] > 3:
                if fixattempt > 0:
                    return False
                else:
                    for z in range(len(report)):
                        report1 = copy.deepcopy(r)
                        report1.pop(z)
                        if check_report(report1, fixattempt+1):
                            return True
                    return False


    return True


for x in range(len(reports)):
    rv[x] = check_report(reports[x], 1)
ans1 = [x for x in rv.values()].count(True)
print("ans1: ", ans1)

for x in range(len(reports)):
    rv[x] = check_report(reports[x])

# for x in rv.keys():
#     if not rv[x]:
#         print(x, reports[x], rv[x])
ans2 = [x for x in rv.values()].count(True)
print("ans2: ", ans2)