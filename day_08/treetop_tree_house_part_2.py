#!/usr/bin/env python3

def is_outside(i, j, trees):
    return i == 0 or i == len(trees) - 1 or j == 0 or j == len(trees[i]) - 1

with open("input.txt", encoding="utf-8") as input:
    trees = list(map(list, input.read().splitlines()))
    scenic_scores = [[0 if is_outside(i, j, trees) else 1 for j in range(len(trees[i]))] for i in range(len(trees))]
    for i in range(1, len(trees) - 1):
        for j in range(1, len(trees[i]) - 1):
            for y in range(j + 1, len(trees[i])):
                if trees[i][y] >= trees[i][j]:
                    break
            scenic_scores[i][j] *= y - j
            for x in range(i + 1, len(trees)):
                if trees[x][j] >= trees[i][j]:
                    break
            scenic_scores[i][j] *= x - i
            for y in range(j - 1, -1, -1):
                if trees[i][y] >= trees[i][j]:
                    break
            scenic_scores[i][j] *= j - y
            for x in range(i - 1, -1, -1):
                if trees[x][j] >= trees[i][j]:
                    break
            scenic_scores[i][j] *= i - x
    print(max(map(max, scenic_scores)))
