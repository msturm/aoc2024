#!/usr/bin/env python3
import requests
import sys
import os
import stat

headers = {
    'User-Agent': 'AoC grabber github.com/msturm/aoc2023',
    'From': 'msturm@wolkje.net'  # This is another valid field
}

if len(sys.argv) < 2:
    print("Missing parameter\nUsage: aoc.py [day]")
    sys.exit(1)

session = ''
with open('session.txt','r') as f:
    session = f.read().strip()

print(session)
year = 2023
day = sys.argv[1]

if os.path.exists('./' + str(day)):
    print("Day {0} is already created".format(day))
    sys.exit(1)


os.mkdir(str(day))
os.chdir(str(day))
url = 'https://adventofcode.com/' + str(year) + '/day/' + str(day) + '/input'
cookies = dict(session = session)

print(url)
r = requests.get(url, allow_redirects=True, cookies = cookies, headers = headers)
open(day + '.in', 'wb').write(r.content)

pythonfile = str(day) + '.py'
open(pythonfile, 'w').write("#!/usr/bin/env python3\nfile1 = '" + str(day) + ".in'\n\n" + "input = [x.strip() for x in open(file1, 'r').readlines()]\nfor v in input:\n")
s = os.stat(pythonfile)
os.chmod(pythonfile, s.st_mode | stat.S_IEXEC)
