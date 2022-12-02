#!/usr/bin/env python3

from enum import Enum
from itertools import cycle

class Shape(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    @classmethod
    def map(cls, encrypted_shape):
        match encrypted_shape:
            case "A" | "X":
                return Shape.ROCK
            case "B" | "Y":
                return Shape.PAPER
            case "C" | "Z":
                return Shape.SCISSORS
            case _:
                raise ValueError("Bad elf!")

    def get_score_against(self, other):
        defeats = {
            Shape.ROCK: Shape.SCISSORS,
            Shape.PAPER: Shape.ROCK,
            Shape.SCISSORS: Shape.PAPER
        }
        if self == other:
            return 3
        elif defeats.get(self) == other:
            return 6
        else:
            return 0

score = 0
with open("input.txt", encoding="utf-8") as input:
    for line in input:
        strategy = list(map(Shape.map, line.split()))
        score += strategy[1].value + strategy[1].get_score_against(strategy[0])
print(score)
