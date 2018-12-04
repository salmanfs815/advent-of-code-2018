#!/bin/python3

import fileinput

def print_fabric(fabric):
    for j in range(len(fabric)):
        for x in fabric[j]:
            print(x, end='')
        print('')
    print('')

def claim(fabric, overlap_count, x, y, w, h):
    # claim w by h square inches of fabric starting from (x,y)
    # (assume origin is top left corner)
    # increment overlap_count for each square inch claimed by at least 2 elves
    for j in range(y, y + h):
        for i in range(x, x + w):
            if fabric[j][i] == '.':
                fabric[j][i] = '#'
            elif fabric[j][i] == '#':
                fabric[j][i] = 'X'
                overlap_count += 1
    return overlap_count

def parse_line(line):
    line = line.split('@')[1].split(':')
    coords = line[0]
    size = line[1]
    x, y = [int(i.strip()) for i in coords.split(',')]
    w, h = [int(i.strip()) for i in size.split('x')]
    return x, y, w, h


def main():
    width = 1000
    height = 1000
    fabric = [['.' for i in range(width)] for j in range(height)]
    overlap_count = 0
    claims = []
    for line in fileinput.input():
        claims.append(line)
    for line in claims:
        x, y, w, h = parse_line(line)
        overlap_count = claim(fabric, overlap_count, x, y, w, h)
        # print(x, y, w, h)
        # print_fabric(fabric)
    print(overlap_count)

if __name__ == "__main__":
    main()
