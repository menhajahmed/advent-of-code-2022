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
            case "A":
                return Shape.ROCK
            case "B":
                return Shape.PAPER
            case "C":
                return Shape.SCISSORS
            case _:
                raise ValueError("Bad elf!")

    def get_shape_to_use(self, result):
        defeats = {
            Shape.ROCK: Shape.SCISSORS,
            Shape.PAPER: Shape.ROCK,
            Shape.SCISSORS: Shape.PAPER
        }
        loses = {
            Shape.ROCK: Shape.PAPER,
            Shape.PAPER: Shape.SCISSORS,
            Shape.SCISSORS: Shape.ROCK
        }
        match result:
            case Result.LOSE:
                return defeats.get(self)
            case Result.DRAW:
                return self
            case Result.WIN:
                return loses.get(self)
            case _:
                raise ValueError("Bad elf!")

class Result(Enum):
    LOSE = 0
    DRAW = 3
    WIN = 6

    @classmethod
    def map(cls, encrypted_result):
        match encrypted_result:
            case "X":
                return Result.LOSE
            case "Y":
                return Result.DRAW
            case "Z":
                return Result.WIN
            case _:
                raise ValueError("Bad elf!")

score = 0
with open("input.txt", encoding="utf-8") as input:
    for line in input:
        strategy = line.split()
        opponent_shape = Shape.map(strategy[0])
        result = Result.map(strategy[1])
        score += opponent_shape.get_shape_to_use(result).value + result.value
print(score)
