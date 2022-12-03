#!/usr/bin/env python3

priority = 0
with open("input.txt", encoding="utf-8") as input:
    for line1 in input:
        rucksack1 = set(line1.strip())
        rucksack2 = set(next(input).strip())
        rucksack3 = set(next(input).strip())
        shared_item_type = next(item_type for item_type in rucksack1
            if item_type in rucksack2 and item_type in rucksack3)
        if shared_item_type.islower():
            priority += ord(shared_item_type) - ord("a") + 1
        else:
            priority += ord(shared_item_type) - ord("A") + 27
print(priority)
