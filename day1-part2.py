#!/bin/python3

import fileinput

frequencies = []

for line in fileinput.input():
    frequencies.append(int(line))

freq_sum = 0
freq_set = {0}
done = False
while not done:
    for freq in frequencies:
        freq_sum += freq
        if freq_sum in freq_set:
            print(freq_sum)
            done = True
            break
        freq_set.add(freq_sum)

