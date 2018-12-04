#!/bin/python3

import fileinput

def print_fabric(fabric):
    for j in range(len(fabric)):
        for x in fabric[j]:
            print(x, end='')
        print('')
    print('')

def claim(fabric, claim_id, x, y, w, h):
    # claim w by h square inches of fabric starting from (x,y)
    # (assume origin is top left corner)
    # increment overlap_count for each square inch claimed by at least 2 elves
    overlap_count = 0
    for j in range(y, y + h):
        for i in range(x, x + w):
            if fabric[j][i] == '.':
                fabric[j][i] = claim_id
            elif type(fabric[j][i]) == int:
                fabric[j][i] = 'X'
                overlap_count += 1
    return overlap_count

def parse_line(line):
    claim_id = int(line.split('@')[0][1:].strip())
    line = line.split('@')[1].split(':')
    coords = line[0]
    size = line[1]
    x, y = [int(i.strip()) for i in coords.split(',')]
    w, h = [int(i.strip()) for i in size.split('x')]
    return claim_id, x, y, w, h

def possible_claims(fabric):
    claims = set()
    for row in fabric:
        for col in row:
            if type(col) == int and col not in claims:
                claims.add(col)
    return claims

def verify_claims(fabric, claims):
    for claim in possible_claims(fabric):
        x, y, w, h = claims[claim]
        potential = True
        j = y
        while potential and j < y + h:
            i = x
            while potential and i < x + w:
                if type(fabric[j][i]) != int:
                    potential = False
                i += 1
            j += 1
        if potential:
            return claim
    return None

def main():
    width = 1000
    height = 1000
    fabric = [['.' for i in range(width)] for j in range(height)]
    overlap_count = 0
    lines = []
    for line in fileinput.input():
        lines.append(line)
    claims = dict()
    for line in lines:
        claim_id, x, y, w, h = parse_line(line)
        claims[claim_id] = (x, y, w, h)
        overlap_count += claim(fabric, claim_id, x, y, w, h)
    valid_claim = verify_claims(fabric, claims)
    print("Valid claim:", valid_claim)

if __name__ == "__main__":
    main()
