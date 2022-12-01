#!/usr/bin/env python3

elf_calories = []
with open("input.txt", encoding="utf-8") as input:
    line = input.readline()
    while line:
        calories = 0
        while line and line != "\n":
            calories += int(line)
            line = input.readline()
        elf_calories.append(calories)
        line = input.readline()
elf_calories.sort()
print(sum(elf_calories[-3:]))
