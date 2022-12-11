#!/usr/bin/env python3

from copy import copy

class Vector:
    x = 0
    y = 0

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def move(self, direction):
        match direction:
            case "U":
                self.y += 1
            case "R":
                self.x += 1
            case "D":
                self.y -= 1
            case "L":
                self.x -= 1
            case _:
                raise ValueError("Unknown direction: " + direction)

    def follow(self, other):
        x_distance = other.x - self.x
        y_distance = other.y - self.y
        abs_x_distance = abs(x_distance)
        abs_y_distance = abs(y_distance)
        if abs_x_distance > 1 or abs_y_distance > 1:
            if x_distance:
                self.x += x_distance // abs_x_distance
            if y_distance:
                self.y += y_distance // abs_y_distance
        return self

with open("input.txt", encoding="utf-8") as input:
    num_knots = 10 # 2 for part 1, 10 for part 2
    knots = [Vector() for _ in range(num_knots)]
    tail_visited = {copy(knots[-1])}
    for line in input:
        direction, steps = line.split()
        for _ in range(int(steps)):
            knots[0].move(direction)
            for i in range(1, len(knots)):
                knots[i].follow(knots[i - 1])
            tail_visited.add(copy(knots[-1]))
    print(len(tail_visited))
