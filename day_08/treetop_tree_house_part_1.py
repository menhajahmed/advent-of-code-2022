#!/usr/bin/env python3

def is_outside(i, j, trees):
    return i == 0 or i == len(trees) - 1 or j == 0 or j == len(trees[i]) - 1

with open("input.txt", encoding="utf-8") as input:
    trees = list(map(list, input.read().splitlines()))
    visible_trees = [[is_outside(i, j, trees) for j in range(len(trees[i]))] for i in range(len(trees))]
    tallest_trees_top = trees[0]
    tallest_trees_bottom = trees[-1]
    for i in range(1, len(trees) - 1):
        tallest_tree_left = trees[i][0]
        tallest_tree_right = trees[i][-1]
        for j in range(1, len(trees[i]) - 1):
            if trees[i][j] > tallest_tree_left:
                tallest_tree_left = trees[i][j]
                visible_trees[i][j] = True
            if trees[i][-j - 1] > tallest_tree_right:
                tallest_tree_right = trees[i][-j - 1]
                visible_trees[i][-j - 1] = True
            if trees[i][j] > tallest_trees_top[j]:
                tallest_trees_top[j] = trees[i][j]
                visible_trees[i][j] = True
            if trees[-i - 1][j] > tallest_trees_bottom[j]:
                tallest_trees_bottom[j] = trees[-i - 1][j]
                visible_trees[-i - 1][j] = True
    print(sum(map(sum, visible_trees)))
