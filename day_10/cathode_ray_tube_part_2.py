#!/usr/bin/env python3

def draw_pixel(cycle, x):
    position = cycle % 40
    print("#" if x - 1 <= position <= x + 1 else ".", end="\n" if position == 39 else "")

with open("input.txt", encoding="utf-8") as input:
    x = 1
    cycle = 0
    for line in input:
        instruction = line.split()
        match instruction[0]:
            case "noop":
                draw_pixel(cycle, x)
                cycle += 1
            case "addx":
                for _ in range(2):
                    draw_pixel(cycle, x)
                    cycle += 1
                x += int(instruction[1])
            case _:
                raise ValueError("Unknown instruction: " + instruction[0])
