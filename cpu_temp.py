#!/usr/bin/python -tt
import re
import subprocess

info = subprocess.getoutput('sensors') 
pattern = '^Core \d:\s+.(\d+)' 

list = []
for line in info.split('\n'):
    match = re.search(pattern,line)
    if match:
        list.append(match.group(1))

print(list[0] + ' ' + list[1])
