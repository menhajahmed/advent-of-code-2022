#!/usr/bin/env python3

priority = 0
with open("input.txt", encoding="utf-8") as input:
    for line in input:
        compartment1 = set(line[:len(line) // 2])
        compartment2 = set(line[len(line) // 2:].strip())
        shared_item_type = next(item_type for item_type in compartment1 if item_type in compartment2)
        if shared_item_type.islower():
            priority += ord(shared_item_type) - ord("a") + 1
        else:
            priority += ord(shared_item_type) - ord("A") + 27
print(priority)
