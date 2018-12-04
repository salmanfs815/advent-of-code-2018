#!/bin/python3

import fileinput

frequencies = []

for line in fileinput.input():
    frequencies.append(line)

print(sum([int(i) for i in frequencies]))

