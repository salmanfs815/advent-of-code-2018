#!/bin/python3

import fileinput

box_ids = []
for line in fileinput.input():
    box_ids.append(line)

length = len(box_ids)

i = 0
while i < length:
    j = i + 1
    while j < length:
        if len([1 for x in zip(box_ids[i], box_ids[j]) if x[0] != x[1]]) == 1:
            print(box_ids[i])
            print(box_ids[j])
            print(''.join([x[0] for x in zip(box_ids[i], box_ids[j]) if x[0] == x[1]]))
            exit(0)
        j += 1
    i += 1

