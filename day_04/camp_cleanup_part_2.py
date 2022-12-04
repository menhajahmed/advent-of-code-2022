#!/usr/bin/env python3

from re import split

overlapping_pairs = 0
with open("input.txt", encoding="utf-8") as input:
    for line in input:
        assignments = list(map(int, split("[-,]", line)))
        if assignments[0] <= assignments[2]:
            a_section_start, a_section_end, b_section_start, b_section_end = assignments
        else:
            b_section_start, b_section_end, a_section_start, a_section_end = assignments
        if a_section_end >= b_section_start:
            overlapping_pairs += 1
print(overlapping_pairs)
