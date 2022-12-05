#!/usr/bin/env python3

from collections import deque
from re import findall

with open("input.txt", encoding="utf-8") as input:
    line = input.readline()
    stacks = [deque() for _ in range((len(line) + 1) // 4)]
    while not line.strip().startswith("1"):
        for i in range(0, len(line), 4):
            if not line[i + 1].isspace():
                stacks[i // 4].appendleft(line[i + 1])
        line = input.readline()
    else:
        stacks = [list(stack) for stack in stacks]
        input.readline()

    for line in input:
        quantity, start, end = map(int, findall(r"\d+", line))
        stacks[end - 1].extend(stacks[start - 1][-quantity:])
        stacks[start - 1] = stacks[start - 1][:-quantity]

    print("".join(stack[-1] for stack in stacks))
