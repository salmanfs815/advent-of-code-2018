#!/bin/python3

import fileinput
from collections import Counter

def exactly2(ids):
    # return count of IDs that have exactly 2 of any letter
    count = 0
    for x in ids:
        d = dict(Counter(x))
        try:
            list(d.keys())[list(d.values()).index(3)]
            count += 1
        except ValueError:
            continue
    return count

def exactly3(ids):
    # return count of IDs that have exactly 3 of any letter
    count = 0
    for x in ids:
        d = dict(Counter(x))
        try:
            list(d.keys())[list(d.values()).index(2)]
            count += 1
        except ValueError:
            continue
    return count


def checksum(ids):
    return exactly2(ids) * exactly3(ids)

box_ids = []
for line in fileinput.input():
    box_ids.append(line)

print(checksum(box_ids))

