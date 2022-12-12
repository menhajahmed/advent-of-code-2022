#!/usr/bin/env python3

from collections import deque

with open("input.txt", encoding="utf-8") as input:
    x = 1
    cycle = 0
    cycles_of_interest = deque((20, 60, 100, 140, 180, 220))
    signal_strength = 0
    for line in input:
        instruction = line.split()
        v = 0
        match instruction[0]:
            case "noop":
                cycle += 1
            case "addx":
                v = int(instruction[1])
                cycle += 2
            case _:
                raise ValueError("Unknown instruction: " + instruction[0])
        while cycles_of_interest and cycle >= cycles_of_interest[0]:
            signal_strength += cycles_of_interest[0] * x
            cycles_of_interest.popleft()
        if not cycles_of_interest:
            break
        x += v
    print(signal_strength)
